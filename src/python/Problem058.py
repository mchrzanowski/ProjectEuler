'''
Created on Jan 30, 2012

@author: mchrzanowski
'''

from ProjectEulerPrime import ProjectEulerPrime
from time import time

RATIO = 0.1

def main():
    start = time()
    primeObject = ProjectEulerPrime()
    
    print "First level with appropriate prime ratio (expressed as a side length): ",
    print determineSpiralLevelWithCorrectRatio(primeObject)
    
    end = time()
    print "Time: ", end - start, " seconds."


def determineSpiralLevelWithCorrectRatio(primeObject):
    
    currentOffsetUsed   = -1   # we skip odd numbers based on the matrix level.
    
    totalSpiralNumbers  = 1
    totalPrimeSpirals   = 0
    
    candidate   = 1
    
    while True:
        # we are looking for two types of odd numbers: the spiral edges and the layer edges. 
        # they are treated slightly differently.
        
        totalSpiralNumbers += 1
        if primeObject.isPrime(candidate):
            totalPrimeSpirals += 1 
            
        sqrtOfCandidate = candidate ** 0.5
        
        if sqrtOfCandidate.is_integer(): # layer edge. update offset to start skipping more odd numbers
            currentOffsetUsed += 1
            if totalPrimeSpirals > 0 and float(totalPrimeSpirals) / totalSpiralNumbers < RATIO:
                return sqrtOfCandidate    # side length of a square is (s^2)^0.5
        
        candidate += 2 * (currentOffsetUsed + 1)

if __name__ == '__main__':
    main()