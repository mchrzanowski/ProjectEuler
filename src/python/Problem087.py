'''
Created on Feb 19, 2012

@author: mchrzanowski
'''

from ProjectEulerPrime import ProjectEulerPrime
from time import time

LIMIT = 5 * 10 ** 7

def main():
    
    start = time()
    
    primeObject = ProjectEulerPrime()
    
    solutionSet = set([])
    
    squareList = [number ** 2 for number in xrange(2, int(LIMIT ** 0.5) + 1) if primeObject.isPrime(number)]
    cubeList = [number ** 3 for number in xrange(2, int(LIMIT ** (1./3)) + 1) if primeObject.isPrime(number)]
    fourthList = [number ** 4 for number in xrange(2, int(LIMIT ** (1./4)) + 1) if primeObject.isPrime(number)]
    
    for square in squareList:
        
        for cube in cubeList:
            
            if square + cube >= LIMIT:
                break
            
            for fourth in fourthList:
                
                resultingSum = square + cube + fourth
                
                if resultingSum >= LIMIT:
                    break
                
                else:
                    solutionSet.add(resultingSum)
                    
    print "Number of sums formed from squared, cubed, and fourthed primes that are < ",LIMIT, " : ", len(solutionSet)
    end = time()
    print "Runtime: ", end - start, " seconds."
    
    

if __name__ == '__main__':
    main()