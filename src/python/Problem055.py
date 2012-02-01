'''
Created on Jan 31, 2012

@author: mchrzanowski
'''

from ProjectEulerLibrary import isNumberPalindromic
from time import time

LIMIT  = 10000
ITERATION_LIMIT = 50

def main():
    
    start = time()
    solutionSet = set([])
    numbersLeadingToPalindromes = set([])
    for i in xrange(1, LIMIT):
        iterationNumber = 0
        candidate = i
        possibleLychrel = True
        iterationIntermediates = set([i])
        
        while iterationNumber < ITERATION_LIMIT:
            
            mirroredNumber = int(str(candidate)[::-1])
            
            newCandidate = candidate + mirroredNumber
            
            if newCandidate in numbersLeadingToPalindromes or isNumberPalindromic(newCandidate):
                possibleLychrel = False
                numbersLeadingToPalindromes ^= iterationIntermediates
                break
            
            candidate = newCandidate
            iterationIntermediates.add(candidate)
            iterationNumber += 1
        
        if possibleLychrel:
            solutionSet.add(i)
    
    end = time()
    
    print "Potential Lychrel numbers < ", LIMIT, " : ", len(solutionSet)
    print "Runtime: ", end - start, " seconds."
    
if __name__ == '__main__':
    main()