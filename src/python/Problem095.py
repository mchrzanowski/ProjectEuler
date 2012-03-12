'''
Created on Mar 11, 2012

@author: mchrzanowski
'''

from ProjectEulerPrime import ProjectEulerPrime
from time import time

LIMIT = 10 ** 6

def getDivisorSum(factors):
    ''' 
    we first create a dict listing the frequency of a prime in the 
    factorization collection. we then apply the formula from:
    http://planetmath.org/encyclopedia/FormulaForSumOfDivisors.html
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
        
    divisorSum = 1
    for prime in frequencyDict:
        divisorSum *= (prime ** (frequencyDict[prime] + 1) - 1) / (prime - 1)
    
    subtractor = 1
    for prime in frequencyDict:
        subtractor *= prime ** frequencyDict[prime]
    
    return divisorSum - subtractor

def createAmicableChain(originalNumber, primeObject, memoizationDict={}):
    
    currentNumber = originalNumber
    chainLinks = set([])

    while currentNumber < LIMIT:
        
        chainLinks.add(currentNumber)
        
        if primeObject.isPrime(currentNumber): return None     # primes have no divisors except 1.

        if currentNumber in memoizationDict:
            divisorSum = memoizationDict[currentNumber]
        else:
            divisorSum = getDivisorSum(primeObject.factorize(currentNumber))
            memoizationDict[currentNumber] = divisorSum
        
        if divisorSum == originalNumber:
            return chainLinks
        elif divisorSum in chainLinks:
            return None                             # we have an infinite chain.
        else:
            currentNumber = divisorSum
    
    return None                                     # we hit a number that is > LIMIT
            
def main():
    
    primeObject = ProjectEulerPrime()
    
    longestChain = []
    
    for i in xrange(2, LIMIT):
        chainLinks = createAmicableChain(i, primeObject)
        if chainLinks is not None and len(chainLinks) > len(longestChain):
            longestChain = chainLinks
           
    
    print "Lowest value:", min(longestChain)
       
    

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."
