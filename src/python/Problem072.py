'''
Created on Feb 11, 2012

@author: mchrzanowski
'''

from ProjectEulerPrime import ProjectEulerPrime
from time import time

LIMIT = 10 ** 6

def main():
    
    start = time()
    
    primeObject = ProjectEulerPrime()
    
    # the question is actually asking for the output of the totient function
    # from 2 to the problem's LIMIT.
    phiList = [1 for number in xrange(LIMIT + 1)]
    
    # defaults.
    phiList[0] = 0
    phiList[1] = 0
        
    for i in xrange(2, LIMIT + 1):
        if primeObject.isPrime(i):
            phiList[i] = i - 1
            for j in xrange(i * 2, len(phiList), i):
                phiList[j] *= float(i - 1) / i
        else:
            phiList[i] *= i
        
    print "Number of reduced, proper fractions where the denominator <= ", LIMIT, " : ", sum([int(round(number, 0)) for number in phiList])
    end = time()
    print "Runtime: ", end - start, " seconds."

if __name__ == '__main__':
    main()