'''
Created on Mar 20, 2012

@author: mchrzanowski
'''

from ProjectEulerPrime import ProjectEulerPrime
from time import time

def getNumberOfDivisors(n, p=ProjectEulerPrime()):
    ''' 
    the formula to get the number of divisors is (n ** 2 + 1) / 2, as given 
    by Euler in http://projecteuler.net/thread=108
    
    we first create a dict listing the frequency of a prime in the 
    factorization collection. the formula to get the number of divisors is:
    (p_1 + 1) * (p_2 + 1) * ... * (p_n + 1)
    where p_i is the frequency of a prime number in a number's factorization
    '''
    n = n ** 2
    factors = p.factorize(n)
        
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
        divisorNumber *= (frequencyDict[prime] + 1) 
        
    return (divisorNumber + 1) / 2

def getNumberOfAdditionPossibilities(n):
    ''' old, slow solution that I found myself '''
    ways = 2    # by default, we can include (1 / n / 2) * 2 and (1 / (n + 1)) + something.
    for i in xrange(n + 2, 2 * n):
        if (float(n * i) / (n - i)).is_integer():
            ways += 1
    return ways

def main():
    
    LIMIT = 10 ** 3
    solution = 0
    iteration = 2
        
    while solution == 0:
        
        if getNumberOfDivisors(iteration) >= LIMIT:
            solution = iteration
        
        iteration += 1
        
    print "Solution: ", solution

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."
