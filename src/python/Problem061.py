'''
Created on Feb 12, 2012

@author: mchrzanowski
'''

import ProjectEulerLibrary
from time import time

def find_cyclic_numbers(listDict):
    
    for number in listDict[8]:  # pick a list to be our driver. might as well be the smallest one.
                
        keysLeft = set([key for key in listDict if key != 8])
        
        cyclicalSet = set([number])
        
        for result in generate_cyclical_set(listDict, keysLeft, number, cyclicalSet):
            return result
                
        
def generate_cyclical_set(listDict, keysLeft, numberToCheckAgainst, cyclicalSet):
    ''' 
    check for all matches to those numbers for which 
    the last 2 numbers of the current number match the first numbers of 
    another number. This is done recursively on whatever lists remain untouched
    until we do a final cyclicality check to make sure all numbers maintain this property
    (including the 'ends'!) 
    '''
    for key in keysLeft:
        for number in listDict[key]:
            if number[1] == numberToCheckAgainst[0]:
                
                newKeySet = set(keysLeft)
                newSet = set(cyclicalSet)

                newKeySet.remove(key)
                newSet.add(number)
                
                for result in generate_cyclical_set(listDict, newKeySet, number, newSet):
                    yield result

    
    if len(keysLeft) ==  0:
        if full_cyclicality_check(cyclicalSet):
            yield cyclicalSet


def full_cyclicality_check(possibleCyclicalSet):
    ''' each number's first and last halves must be present
    in other numbers of the set. so just loop through the set 
    with at most two sub loops to do the verification.'''
    
    isSetAFullCycle = True
    
    for possibleCyclicalNumber in possibleCyclicalSet:

        isFirstHalfGood = False
        isSecondHalfGood = False
            
        for otherNumber in possibleCyclicalSet:
            if otherNumber == possibleCyclicalNumber:
                continue
            if possibleCyclicalNumber[1] == otherNumber[0]:
                isFirstHalfGood = True
                break
        
        if not isFirstHalfGood:
            isSetAFullCycle = False
            break 
         
        for otherNumber in possibleCyclicalSet:
            if possibleCyclicalNumber == otherNumber:
                continue
            if possibleCyclicalNumber[0] == otherNumber[1]:
                isSecondHalfGood = True
                break
            
        if not isSecondHalfGood:
            isSetAFullCycle = False
            break
        
    if isSetAFullCycle:
        return True
    
    else:
        return False
            
def main():
    start = time()
    
    LIMIT  = 10 ** 3
    START_LIMIT = 10 ** 3
    END_LIMIT = 9999
    
    listDict = {}
    
    listDict[3] = [tuple([str(number)[:2], str(number)[2:]]) for number in ProjectEulerLibrary.generateTriangleNumbers(LIMIT) if number <= END_LIMIT and number > START_LIMIT]
    listDict[4] = [tuple([str(number)[:2], str(number)[2:]]) for number in ProjectEulerLibrary.generateSquareNumbers(LIMIT) if number <= END_LIMIT and number > START_LIMIT]
    listDict[5] = [tuple([str(number)[:2], str(number)[2:]]) for number in ProjectEulerLibrary.generatePentagonalNumbers(LIMIT) if number <= END_LIMIT and number > START_LIMIT]
    listDict[6] = [tuple([str(number)[:2], str(number)[2:]]) for number in ProjectEulerLibrary.generateHexagonalNumbers(LIMIT) if number <= END_LIMIT and number > START_LIMIT]
    listDict[7] = [tuple([str(number)[:2], str(number)[2:]]) for number in ProjectEulerLibrary.generateHeptagonalNumbers(LIMIT) if number <= END_LIMIT and number > START_LIMIT]
    listDict[8] = [tuple([str(number)[:2], str(number)[2:]]) for number in ProjectEulerLibrary.generateOctagonalNumbers(LIMIT) if number <= END_LIMIT and number > START_LIMIT]
        
    cyclicalSet =  find_cyclic_numbers(listDict)
    
    
    print "Sum of cyclical set of number: ", sum([int(''.join(number)) for number in cyclicalSet])
    end = time()
    print "Runtime: ", end - start, " seconds."

if __name__ == '__main__':
    main()