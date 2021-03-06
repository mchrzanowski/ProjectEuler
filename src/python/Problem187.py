'''
Created on Feb 21, 2012

@author: mchrzanowski
'''

from math import sqrt
from ProjectEulerLibrary import pi, sieveOfEratosthenes
from time import time

LIMIT = 10 ** 8


def main():
    '''
    formula given by MathWorld:
    http://mathworld.wolfram.com/Semiprime.html
    '''

    # first, get all primes < sqrt(LIMIT).
    # place a 0 at index 0 for easier indexing.
    primesFound = [0]
    primesFound.extend(sieveOfEratosthenes(sqrt(LIMIT)))

    solution = 0
    for i in xrange(1, len(primesFound)):
        solution += pi(LIMIT / primesFound[i]) - i + 1

    print "Found:", solution, "composites formed from 2 primes."


if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime: ", end - start, " seconds."
