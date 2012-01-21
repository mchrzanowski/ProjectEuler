'''
Created on Jan 20, 2012

@author: mchrzanowski
'''

from time import time
from ProjectEuler import isNumberPalindromic

LIMIT = 1000000


def main():
    start = time()
    solutions = set([])
    for i in xrange(1, LIMIT):
        if isNumberPalindromic(i) and isNumberPalindromic(str(bin(i))[2:]):
            solutions.add(i)
    
    print "Sum of solution set: ", sum(solutions)
    end = time()
    print "Runtime: ", end - start, " seconds."

if __name__ == '__main__':
    main()