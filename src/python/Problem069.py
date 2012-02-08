'''
Created on Feb 7, 2012

@author: mchrzanowski
'''

from ProjectEulerPrime import ProjectEulerPrime
from time import time

LIMIT = 1000000

def main():
    
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
    
    

if __name__ == '__main__':
    main()