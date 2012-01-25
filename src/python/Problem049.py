'''
Created on Jan 23, 2012

@author: mchrzanowski
'''

from ProjectEulerPrime import ProjectEulerPrime
from time import time

SEQUENCE_LIMIT = 3
LIMIT = 9999
START = 1111

def constructPrimeMap(primeObject, primeDict):
    ''' construct lists of all prime numbers. group by character types. 
    use a sorted character group as a key '''

    for i in xrange(START, LIMIT + 1):
        stringifiedNumber = str(i)
        if '0' in stringifiedNumber:
            continue
        if primeObject.isPrime(i):
            listOfNumbers = [char for char in stringifiedNumber]
            listOfNumbers.sort()
            key = int(''.join(listOfNumbers))
            if key not in primeDict:
                primeDict[key] = []
            primeDict[key].append(i)


def discoverArithmeticSequences(primeDict, solutionSet):
    ''' for each element in a list, find the difference between it and a base element .
    look for differences that are even and present in the hashes already '''
    for key in primeDict:
        if len(primeDict[key]) < SEQUENCE_LIMIT:
            continue
        
        primeDict[key].sort()        
        for i in xrange(len(primeDict[key]) - 2):
            
            sequenceOccurrenceDict = {}
            for j in xrange(i + 1, len(primeDict[key])):
                                
                difference = primeDict[key][j] - primeDict[key][i]
    
                if difference not in sequenceOccurrenceDict:
                    sequenceOccurrenceDict[difference] = []
                    sequenceOccurrenceDict[difference].append(primeDict[key][i])
                
                sequenceOccurrenceDict[difference].append(primeDict[key][j])
                
                #the distance from 1 to 3 should be exactly double the distance from 1 to 2
                halfDifference = difference / 2;
                
                if halfDifference in sequenceOccurrenceDict:
                    sequenceOccurrenceDict[halfDifference].append(primeDict[key][j])
                                
            for k in sequenceOccurrenceDict:
                if len(sequenceOccurrenceDict[k]) == SEQUENCE_LIMIT:
                    solutionSet.add(tuple(sequenceOccurrenceDict[k]))

def main():
    start = time()
    primeObject = ProjectEulerPrime()
    solutionSet = set([])
    primeDict = {}
    constructPrimeMap(primeObject, primeDict)
    discoverArithmeticSequences(primeDict, solutionSet)
    
    for solution in solutionSet:
        print "Concatenated tuple: ", ''.join([str(number) for number in solution])
        
    end = time()
    print "Runtime: ", end - start, " seconds."   

if __name__ == '__main__':
    main()