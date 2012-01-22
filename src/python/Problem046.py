'''
Created on Jan 21, 2012

@author: mchrzanowski
'''

from time import time
from math import sqrt, ceil
from ProjectEulerLibrary import isPrime

def main():
    
    start = time()
    
    primeSet = set([])
    squaredDict = {}

    candidate   = 5
    solution    = 0
    
    while solution == 0:
        if candidate not in primeSet and not isPrime(candidate):
            createdUsingPrime = False
            for i in xrange(1, int(ceil(sqrt(candidate / 2)))): # only check natural numbers for primality
                
                if i not in squaredDict:
                    squaredDict[i] = 2 * i ** 2                    
                
                remainderValue = candidate - squaredDict[i]
                                
                if remainderValue in primeSet or isPrime(remainderValue):
                    primeSet.add(remainderValue)
                    createdUsingPrime = True
                    break

            
            if not createdUsingPrime:
                solution = candidate
                
        else:
            primeSet.add(candidate)
        
        candidate += 2
            
    print "Smallest odd, composite number that breaks the conjecture: ", solution     
        
    end = time()
    
    print "Runtime: ", end - start, " seconds."
    
if __name__ == '__main__':
    main()
