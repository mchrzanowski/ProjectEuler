'''
Created on Jan 22, 2012

@author: mchrzanowski
'''

from time import time
from Prime import Prime

PRIME_LIMIT = 4

def main():
    
    start = time()
    primeFactorizationDict = {}
    p = Prime()
    firstOfFour = 0
    candidate = 210     # 210 is the product of the smallest 4 unique primes
    while firstOfFour == 0:
        
        if p.factor(candidate):
        
            if candidate not in primeFactorizationDict:
                primeFactorizationDict[candidate] = len(set([prime for prime in p.factorize(candidate)]))
            if primeFactorizationDict[candidate] == PRIME_LIMIT:
                if candidate + 1 not in primeFactorizationDict:
                    primeFactorizationDict[candidate + 1] = len(set([prime for prime in p.factorize(candidate + 1)]))
                if primeFactorizationDict[candidate + 1] == PRIME_LIMIT:
                    if candidate + 2 not in primeFactorizationDict:
                        primeFactorizationDict[candidate + 2] = len(set([prime for prime in p.factorize(candidate + 2)]))
                    if primeFactorizationDict[candidate + 2] == PRIME_LIMIT:
                        if candidate + 3 not in primeFactorizationDict:
                           primeFactorizationDict[candidate + 3] = len(set([prime for prime in p.factorize(candidate + 3)]))
                        if primeFactorizationDict[candidate + 3] == PRIME_LIMIT:
                            firstOfFour = candidate
       
        candidate += 1
    end = time()
    print "First of four integers: ", firstOfFour
    print "Runtime: ", end - start, " seconds. "

if __name__ == '__main__':
    main()