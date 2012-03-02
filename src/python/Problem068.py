'''
Created on Feb 29, 2012

@author: mchrzanowski
'''

from time import time


NUMBER_LIMIT = 10
SOLUTION_SIZE = 16
GON_NUMBER = NUMBER_LIMIT / 2

def initializeSummationDict():
    
    summationDict = {}
    for i in xrange(1, NUMBER_LIMIT - 1):
        for j in xrange(i + 1, NUMBER_LIMIT):
            for k in xrange(j + 1, NUMBER_LIMIT + 1):
                key = i + j + k
                if key not in summationDict: summationDict[key] = set()
                summationDict[key].add(frozenset([i, j, k]))
    return summationDict


def createInitialSolutionDict(initialDict):
    ''' 
    Take the initial sets and produce potential pentagon triplets from them. This means 
    that we will get lists of 5 sets of numbers, each of which sum to a total, and which at least form a ring
    '''

    solutionDict = {}
    for key in initialDict:
        for summedSet in initialDict[key]:
            setCopy = initialDict[key].copy()
            setCopy.remove(summedSet)
            for solutionList, solutionJoinPoints in createPentagons(setCopy, [summedSet]):
                if key not in solutionDict: 
                    solutionDict[key] = set([])
                solutionDict[key].add(frozenset(solutionList))
    
    return solutionDict
    
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

def postProcess(solutionDict):
    ''' get rid of as many cases that don't fullfill our requirements as possible.'''
    incompleteRangePurge(solutionDict)
    joinFrequencyPurge(solutionDict)
    correctConcatLengthPurge(solutionDict)
    
def incompleteRangePurge(solutionDict):
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
    ''' check to see if we add up to the solution number. if not, skip. '''
    for key in solutionDict:
        for sequenceCollection in solutionDict[key].copy():
            numberList = []
            for sequence in sequenceCollection:
                for number in sequence:
                    numberList.append(number)
            if len(''.join([str(number) for number in numberList])) != SOLUTION_SIZE:
                solutionDict[key].remove(sequenceCollection)    

def main():
            
    # create sets of numbers that sum to a given number
    
    solutionDict = createInitialSolutionDict(initializeSummationDict())
    
    postProcess(solutionDict)
        
    printState(solutionDict)
    
def printState(solutionDict):
    for key in solutionDict: 
        for value in solutionDict[key]:
            print key, ":", value

def createPentagons(setsLeft, listOfJoinedSets, joinPoints=[]):
        
    # almost done! we just need to link the ring together.
    if len(joinPoints) == GON_NUMBER - 1:
        
            
            intersection = set(listOfJoinedSets[-1]).intersection(listOfJoinedSets[0])
                        
            if len(intersection) == 1:
                
                    yield listOfJoinedSets, joinPoints
        
    else:
          
        for nextSet in setsLeft:
           
            intersection = nextSet.intersection(listOfJoinedSets[-1])
            
            for number in intersection:
                
                if number not in joinPoints:
                    
                    # prepare for recursive call.
                    joinPointsCopy = list(joinPoints)
                    joinPointsCopy.append(number)
                    
                    listOfJoinedSetsCopy = list(listOfJoinedSets)
                    listOfJoinedSetsCopy.append(nextSet)
                    
                    setsLeftCopy = set(setsLeft)
                    setsLeftCopy.remove(nextSet)
                    
                    for listOfSets, newJoinPoints in createPentagons(setsLeftCopy, listOfJoinedSetsCopy, joinPointsCopy):
                        yield listOfSets, newJoinPoints
            

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."