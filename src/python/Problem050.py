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
    primeList = []                      # not quite sure if this proof is rigorous enough, but numerical analysis verified it:
    for i in xrange(LIMIT / 21 + 1):    # the problem says that there are 21 primes in a sequence that produces 953. 
                                        # so we know that there has to be at least a 21 prime sequence in a prime < million.
        if primeObject.isPrime(i):      # each prime has to therefore be at most 1/21 of the series' summation.
            primeList.append(i)         # in fact, since 1_000_000 is not iself a prime, this is an upper bound.
    
    maxNumberOfPrimes = 0
    maxPrime = 0
    
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