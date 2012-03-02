'''
Created on Feb 29, 2012

@author: mchrzanowski
'''

from time import time

NUMBER_LIMIT = 10
SOLUTION_SIZE = 16
GON_NUMBER = NUMBER_LIMIT / 2

def initializeSummationDict():
    ''' create all possible combinations of all possible totals using 3 numbers from 1..NUMBER_LIMIT'''
    summationDict = {}
    for i in xrange(1, NUMBER_LIMIT - 1):
        for j in xrange(i + 1, NUMBER_LIMIT):
            for k in xrange(j + 1, NUMBER_LIMIT + 1):
                key = i + j + k
                if key not in summationDict: summationDict[key] = set()
                summationDict[key].add(frozenset([i, j, k]))
    return summationDict

def createSolutions(initialDict):
    ''' 
    Take the initial sets and produce potential pentagon triplets from them. This means 
    that we will get lists of 5 sets of numbers, each of which sum to a total, and which at least form a ring.
    return the sets and the join points of the ring as separate dicts for ease of use by me.
    '''

    solutionDict = {}
    joinDict = {}
    for key in initialDict:
        for summedSet in initialDict[key]:
            setCopy = initialDict[key].copy()
            setCopy.remove(summedSet)
            for solutionList, solutionJoinPoints in createPentagons(setCopy, [summedSet]):
                if key not in solutionDict: 
                    solutionDict[key] = set([])
                    joinDict[key] = set([])
                solutionDict[key].add(frozenset(solutionList))
                joinDict[frozenset(solutionList)] = frozenset(solutionJoinPoints)
    
    return solutionDict, joinDict
    
def joinFrequencyPurge(solutionDict):
    ''' join numbers must be listed twice in the full collection. the rest once only. '''
    for key in solutionDict:
        for sequenceList in solutionDict[key].copy():
            frequencyDict = {}
            for sequence in sequenceList:
                for number in sequence:
                    if number not in frequencyDict: frequencyDict[number] = 0
                    frequencyDict[number] += 1
            
            numberEqualToTwo = 0
            numberEqualToOne = 0
            for numberKey in frequencyDict:
                if frequencyDict[numberKey] == 2: 
                    numberEqualToTwo += 1
                elif frequencyDict[numberKey] == 1:
                    numberEqualToOne += 1
            
            if not numberEqualToTwo == numberEqualToOne == GON_NUMBER:
                solutionDict[key].remove(sequenceList)

def postProcessPurge(solutionDict):
    ''' get rid of as many cases that don't fullfill our requirements as possible.'''
    rangePurge(solutionDict)
    joinFrequencyPurge(solutionDict)
    correctConcatLengthPurge(solutionDict)
      
def rangePurge(solutionDict):
    '''the 5 sets must at least include each number from 1..LIMIT at least once.'''
    referenceNumberSet = frozenset([number for number in xrange(1, NUMBER_LIMIT + 1)])
    
    for key in solutionDict:
        for sequenceList in solutionDict[key].copy():
            representedNumberSet = set()
            for sequence in sequenceList:
                for number in sequence:
                    representedNumberSet.add(number)
            if representedNumberSet != referenceNumberSet:
                solutionDict[key].remove(sequenceList)

def correctConcatLengthPurge(solutionDict):
    ''' check to see if our stringified numbers are of the proper solution size. if not, skip. '''
    for key in solutionDict:
        for sequenceCollection in solutionDict[key].copy():
            numberList = []
            for sequence in sequenceCollection:
                for number in sequence:
                    numberList.append(number)
            if len(''.join([str(number) for number in numberList])) != SOLUTION_SIZE:
                solutionDict[key].remove(sequenceCollection)    

def constructSolutionString(sequenceCollection, joinPoints, resultList=[]):
    '''
    the algorithm here exploits the fact that in a legal ring, for a given sequence,
    one number will be the outlier and the other two values will be join points. 
    
    so to start it off, we look for the sequence with the smallest possible outlier.
    since we want max strings, we reverse-sort the last two values to get the highest number.
    
    from there, to go clockwise, we observe that the last value of this first sequence must be the middle 
    value of some other sequence in the ring. 
    
    so we recurse and add the outlier, middle, and end values of all subsequent
    sequences in that order to a list that's returned back to the caller.
    ''' 
    sequenceCollection = set(sequenceCollection)
    
    if len(resultList) == 0:    # find the smallest outlier.
        lowestOutlier = NUMBER_LIMIT + 1
        for sequence in sequenceCollection:
            for number in sequence:
                if number not in joinPoints and number < lowestOutlier:
                    lowestOutlier = number
                    minimumSequence = sequence
                    break    # 1 such number per sequence.
        
        
        sequence = list(minimumSequence)
        sequence.remove(lowestOutlier)
        resultList.append(lowestOutlier)
        
        # there are now 2 number left in the sequence. reverse-sort it.
        sequence.sort(reverse = True)
        resultList.extend(sequence)
        
        sequenceCollection.remove(minimumSequence)
        
        # recurse.
        return constructSolutionString(sequenceCollection, joinPoints, resultList)
        
    elif len(sequenceCollection) == 0:
        listToReturn = list(resultList)
        del resultList[:]   # remove the method's state.
        return listToReturn
    
    else:  
        # the last element of resultList *must* be the middle value of another 3-pair list.
        # and the value in that 3-pair list that is not in the joinPoints set is the outlying value.
        for sequence in sequenceCollection.copy():
            if resultList[-1] in sequence:
                mutableSequence = set(sequence)
                for number in mutableSequence.copy():
                    if number not in joinPoints:
                        resultList.append(number)   # the outlier value has been found.
                        mutableSequence.remove(number)
                        break
                
                resultList.append(resultList[-2])   # now append the joining value as the middle number of the next 3-pair
                mutableSequence.remove(resultList[-3])
                
                resultList.append(mutableSequence.pop())   # and, finally, get the last value.
                sequenceCollection.remove(sequence)
                break

        return constructSolutionString(sequenceCollection, joinPoints, resultList)

def main():
            
    # create sets of numbers that sum to a given number
    
    solutionDict, joinPointDict = createSolutions(initializeSummationDict())
    
    postProcessPurge(solutionDict)
    
    maximumTotal = 0
    
    for key in solutionDict:
        for collection in solutionDict[key]:
            newList = constructSolutionString(collection, joinPointDict[collection])
            integerizedSolution = int(''.join([str(number) for number in newList]))
            if integerizedSolution > maximumTotal:
                maximumTotal = integerizedSolution
    
    print "Maximum",SOLUTION_SIZE,"- length number:",maximumTotal 
            
def printState(solutionDict):
    for key in solutionDict: 
        for value in solutionDict[key]:
            print key, ":", value

def createPentagons(sequencesLeft, listOfJoinedSequences, joinPoints=[]):
    ''' of the sets that have been created, we only need n to create a n-gon ring.
    so recursively check all possible combinations to create a ring structure from the sequences available.
    
    this basically means that each sequence needs to intersect with another sequence using a join value that is not
    already being used as a join point in the ring. and, of course, the nth sequence must connect to the first sequence
    '''
    # almost done! we just need to link the ring together, if possible.
    if len(joinPoints) == GON_NUMBER - 1:
        
        intersection = set(listOfJoinedSequences[-1]).intersection(listOfJoinedSequences[0])
                    
        if len(intersection) == 1:
            
                joinPoints.append(intersection.pop())
            
                yield listOfJoinedSequences, joinPoints
        
    else:
          
        for sequence in sequencesLeft:
           
            intersection = sequence.intersection(listOfJoinedSequences[-1])
            
            for number in intersection:
                
                if number not in joinPoints:
                    
                    # prepare for recursive call.
                    joinPointsCopy = list(joinPoints)
                    joinPointsCopy.append(number)
                    
                    listOfJoinedSetsCopy = list(listOfJoinedSequences)
                    listOfJoinedSetsCopy.append(sequence)
                    
                    sequencesLeftCopy = set(sequencesLeft)
                    sequencesLeftCopy.remove(sequence)
                    
                    for listOfSequences, newJoinPoints in createPentagons(sequencesLeftCopy, listOfJoinedSetsCopy, joinPointsCopy):
                        yield listOfSequences, newJoinPoints

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."
    