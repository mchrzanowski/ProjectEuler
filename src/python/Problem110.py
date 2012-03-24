'''
Created on Mar 23, 2012

@author: mchrzanowski
'''

from operator import mul
from ProjectEulerPrime import ProjectEulerPrime
from time import time

def getNumberOfDivisors(factors):
    '''
    algo is: (tau(n ** 2) + 1 ) / 2, as given by:
    http://oeis.org/A018892
    the input to this function is 
    the factorization of a given n.
    '''
    def getFrequency(factors):
        frequencyDict = {}
        for factor in factors:
            if factor in frequencyDict:
                frequencyDict[factor] += 1 
            else: 
                frequencyDict[factor] = 1
        return frequencyDict
    
    frequencyDict = getFrequency(factors)

    divisorNumber = 1
    for prime in frequencyDict:
        divisorNumber *= (2 * frequencyDict[prime] + 1)     # factorization of (n ** 2) = (factorization of n) * 2
        
    return (divisorNumber - 1) / 2

def getUniqueFactorization(n, p=ProjectEulerPrime()):
    '''  return a list of unique primes whose divisor number is >= n '''
    if n < 2: return []
    factors = [2]
    iteration = 1

    while getNumberOfDivisors(factors) < n:
        iteration += 2
        while not p.isPrime(iteration): iteration += 2  # find the next prime.
        factors.append(iteration)
    
    return factors

def main():
    
    LIMIT = 4 * 10 ** 6
    p = ProjectEulerPrime()
    
    # using an algo inspired by hk:
    # http://projecteuler.net/thread=108
    
    # first step: get a product of unique primes
    # such that the number of divisors is >= LIMIT.
    factors = getUniqueFactorization(LIMIT, p) 
    
    # second step: start minimizing the divisor number with a floor of LIMIT
    # do this by removing the largest prime and replacing it with 
    # a group of primes s.t. their product is < the largest prime.

    bestDivisorNumber = getNumberOfDivisors(factors)
    bestFactorization = factors
        
    for largestPrime in reversed(factors):       # we need to try to replace each original prime once.
                
        iterationBestDivisorNumber = bestDivisorNumber  # these are used so as to not update the absolute minimized factorization
        iterationBestFactorization = bestFactorization  # until we finish a loop.
        
        for i in xrange(4, largestPrime):   # optimization: skip 2 and 3 as we can't replace primes with another prime.
            
            if p.isPrime(i): continue       # skip primes.
            
            newFactorization = p.factorize(i)
            
            newFactorization.extend(bestFactorization)
            newFactorization.remove(largestPrime)            
            newDivisorNumber = getNumberOfDivisors(newFactorization)
                        
            if newDivisorNumber >= LIMIT and newDivisorNumber < iterationBestDivisorNumber:
                iterationBestFactorization = newFactorization
                iterationBestDivisorNumber = newDivisorNumber
                
        bestFactorization = iterationBestFactorization
        bestDivisorNumber = iterationBestDivisorNumber
         
        
    print "Lowest number with >=",LIMIT,"possible 2 unit fraction additions: ", reduce(mul, bestFactorization)
    print "Number of additions: ", bestDivisorNumber

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."
