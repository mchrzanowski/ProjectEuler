'''
Created on Mar 25, 2012

@author: mchrzanowski
'''

from ProjectEulerPrime import ProjectEulerPrime
from time import time


def getNextPrime(beginning, p=ProjectEulerPrime()):
    ''' get the next prime after an input: beginning '''
    i = beginning    
    nextPrime = 0
    while nextPrime == 0:
        i += 1
        if p.isPrime(i): 
            nextPrime = i

    return nextPrime
        
def main():
    
    LIMIT = 10 ** 10
    p = ProjectEulerPrime()
    
    # the algo is : remainder = p(n) * n * 2
    # where p(n) is the nth prime
    
    n = 3
    prime = 5
    solution = 0
        
    while solution == 0:
        
        prime = getNextPrime(prime, p)
        n += 1
        
        if n & 1 != 0:                  # the remainder for all even n from this formula is 2
            if prime * 2 * n >= LIMIT:
                solution = n     
    
    print "Solution: ", solution

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime: ", end - start, "seconds."