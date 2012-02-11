'''
Created on Feb 7, 2012

@author: mchrzanowski
'''

from ProjectEulerPrime import ProjectEulerPrime
from time import time

LIMIT = 1000000

def slowAlgorithm():
    
    start = time()
    primeObject = ProjectEulerPrime()
    
    maxValue = LIMIT + 1
    maxRatio = 0
        
    for i in xrange(2, LIMIT + 1):
        # Euler's product formula:
        # phi(n) = n * product((1 - (1 / unique prime divisors))
        phi = i
        for prime in set(primeObject.factorize(i)):
            phi *= 1 - float(1) / prime
        
        if i / phi > maxRatio:
            maxRatio = i / phi
            maxValue = i
            
    end = time()
    print "Value for which ratio is maximized: ", maxValue
    print "Runtime: ", end - start, " seconds."

def main():
    
    start = time()
    primeObject = ProjectEulerPrime()
    
    # so, my first attempt at this used Euler's product formula and was really slow.
    # Thanks to the people in the forum of P69 of Project Euler for help with this.
    # we want to maximize n / phi(n). phi(n) = n * product((prime - 1)/prime) for each prime
    # therefore, we want to maximize 1 / product((prime - 1)/prime) for each prime
    # let's think about the most naive strategy to get these primes: get the first x primes whose product <= LIMIT
    # if we were to swap even one of the small primes in this list with a slightly larger prime, then 
    # product((prime - 1)/prime) for each prime would actually get bigger. 
    # thus making 1 / product((prime - 1)/prime) for each prime smaller. 
    # therefore, we just get the first couple primes whose product is <= LIMIT.
    
    product = 2
    for i in xrange(3, LIMIT + 1, 2):
        if product * i > LIMIT:
            break
        if primeObject.isPrime(i):
            product *= i
        
    end = time()
    print "Value for which ratio is maximized: ", product
    print "Runtime: ", end - start, " seconds."
    
if __name__ == '__main__':
    main()