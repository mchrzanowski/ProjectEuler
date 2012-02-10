'''
Created on Feb 9, 2012

@author: mchrzanowski
'''

from math import factorial
from time import time

LIMIT = 1000000
CYCLE_LIMIT = 60

def main():
    
    start = time()
    
    solutions = 0
    
    factorialDict = {}
    for i in xrange(10):
        factorialDict[str(i)] = factorial(i)
    
    termDict = {}       # for memoization
    
    for i in xrange(1, LIMIT + 1):
        
        currentTerm = str(i)
        
        termSet = set([currentTerm])
        
        numberOfTerms = 1   # it should reflect the length of termSet + whatever the memoization provides
        
        while True:
            
            newNumber = str(sum([factorialDict[char] for char in currentTerm]))
            
            if newNumber in termDict:
                numberOfTerms += termDict[newNumber]
                break
 
            if newNumber not in termSet:
                termSet.add(newNumber)
                numberOfTerms += 1
            
            else:
                break
            
            currentTerm = newNumber
        
        termDict[str(i)] = numberOfTerms
        
        if numberOfTerms == CYCLE_LIMIT:
            solutions += 1
    
    print "Number of chains == ", CYCLE_LIMIT, " : ", solutions
    end = time()
    print "Runtime: ", end - start, " seconds."
        
    

if __name__ == '__main__':
    main()