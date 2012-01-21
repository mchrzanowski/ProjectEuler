'''
Created on Jan 19, 2012

@author: mchrzanowski
'''

from ProjectEuler import isPrime
from time import time

LIMIT  = 1000000

def main():
    
    start = time()
    primeSet = set([])
    solutionSet = set([])
    
    for i in xrange(2, LIMIT + 1):
        if isPrime(i):
           primeSet.add(str(i)) 
               
    for prime in primeSet:
        tempPrime = prime
        isSolution = True
        for iteration in xrange(len(prime) - 1):
            tempPrime = tempPrime[1:] + tempPrime[0]
            if tempPrime not in primeSet:
                isSolution = False
                break
        if isSolution:
            solutionSet.add(prime)
    
    print "Solution set size: ", len(solutionSet)
    
    end = time()
    print "Runtime: ", end - start, " seconds."


if __name__ == '__main__':
    main()