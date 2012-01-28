'''
Created on Jan 26, 2012

@author: mchrzanowski
'''

from ProjectEulerPrime import ProjectEulerPrime
from time import time

def main():
    start = time()
    primeObject = ProjectEulerPrime()
    primeSet = set([])
    for i in xrange(10000001, 11000000, 2):
        if primeObject.isPrime(i):
            primeSet.add(i)
    
    end = time()
    print "Runtime: ", end - start, " seconds."

if __name__ == '__main__':
    main()