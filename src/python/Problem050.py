'''
Created on Jan 24, 2012

@author: mchrzanowski
'''
from time import time
from ProjectEulerPrime import ProjectEulerPrime

LIMIT = 1000000

def main():
    start = time()
    primeObject = ProjectEulerPrime()
    primeList = [2]                     # 2 is the only even prime.           
    for i in xrange(3, LIMIT / 183, 2): # interesting pattern:  
                                        # all primes will be in the range of numbers 
        if primeObject.isPrime(i):      # LIMIT / (number of prime terms in the series for LIMIT / 10 )
            primeList.append(i)         # so 10 = 10 / 1, 100 = 100 / 2, 1000 = 1000 / 6, 10000 = 10000 / 21, 
                                        # 100000 = 100000 / 65, 1000000 = 1000000 / 183 and so on for at least 100M.
    maxPrime = 0
    maxNumberOfPrimes = 0
    
    for i in xrange(len(primeList)):
        currentPrimeSequence = [primeList[i]]
        currentSum = primeList[i]
        
        for j in xrange(i + 1, len(primeList)):
            currentSum += primeList[j]
            currentPrimeSequence.append(primeList[j])
            if currentSum < LIMIT and primeObject.isPrime(currentSum):
                 if len(currentPrimeSequence) > maxNumberOfPrimes:
                     maxNumberOfPrimes = len(currentPrimeSequence)
                     maxPrime = sum(currentPrimeSequence)
            elif currentSum >= LIMIT:
                break
            
    print "Longest number of sequential primes that sum to a prime: ", maxNumberOfPrimes
    print "Sum: ", maxPrime
    end = time()
    print "Runtime: ", end - start, " seconds."

if __name__ == '__main__':
    main()