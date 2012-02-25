'''
Created on Feb 24, 2012

@author: mchrzanowski

http://projecteuler.net/problem=77

'''

from ProjectEulerPrime import ProjectEulerPrime
from time import time

LIMIT = 10 ** 2             # this number can't be that huge; the sequence is very non-linear.
SUM_LIMIT = 5 * 10 ** 3     # by 20, it's at 26. by 50, it's already at 819. so 100 seems like a very safe ceiling.

def main():
    
    primeObject = ProjectEulerPrime()
    
    solution = 0
    
    numberOfWays = [0 for i in xrange(LIMIT + 1)]
    
    numberOfWays[0] = 1     # start it off
    
    for i in xrange(2, LIMIT + 1):
        
        if primeObject.isPrime(i):
            
            for j in xrange(i, LIMIT + 1): numberOfWays[j] += numberOfWays[j - i]
        
        if numberOfWays[i] >= SUM_LIMIT:
            solution = i
            break
    
    print "First number to be produced", SUM_LIMIT, "different ways using sums of primes:", solution 

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."