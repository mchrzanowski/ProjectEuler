'''
Created on Feb 10, 2012

@author: mchrzanowski
'''

from ProjectEulerPrime import ProjectEulerPrime
from time import time

LIMIT = 10 ** 7
RANGE_LIMIT = 10 ** 3
RANGE_INCREMENT = 10 ** 2

def main():
    
    start = time()
    primeObject = ProjectEulerPrime()
    
    minRatio = LIMIT
    minValue = LIMIT
    
    sqrtOfLimit = int(LIMIT ** 0.5)
    # since phi(n) = n - 1 when n == prime, phi(n) can't ever be a permutation of n.
    # the next best thing is a pair of primes.
    # since n / phi(n) means being as close to 1 as possible, look for numbers around sqrt(LIMIT)
    
    rangeToConsider = RANGE_INCREMENT
    
    while rangeToConsider < RANGE_LIMIT:
        
        for i in xrange(sqrtOfLimit - rangeToConsider, sqrtOfLimit, 1):
            
            if primeObject.isPrime(i):
                
                for j in xrange(sqrtOfLimit + rangeToConsider, sqrtOfLimit, -1):
                    
                    candidateProduct = i * j
                    
                    if candidateProduct > LIMIT:
                        continue
                    
                    if primeObject.isPrime(j):
                        
                        phi = round(i * j * float(i - 1) / i * float(j - 1) / j, 0)
                                                                                                
                        if i * j / phi < minRatio:
                            
                            candidateCharList = [char for char in str(i * j)]       
                            phiCharList = [char for char in str(int(phi))]
                            
                            candidateCharList.sort()
                            phiCharList.sort()
                                                    
                            if candidateCharList == phiCharList:
                                minRatio = i * j / phi
                                minValue = i * j
                
        rangeToConsider += RANGE_INCREMENT
    
        
    
    end = time()
    print "Value for which ratio is minimized: ", minValue
    print "Runtime: ", end - start, " seconds."

if __name__ == '__main__':
    main()