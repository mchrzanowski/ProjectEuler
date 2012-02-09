'''
Created on Feb 9, 2012

@author: mchrzanowski
'''

from fractions import gcd
from math import ceil
from time import time

LIMIT = 12000

def main():
    start = time()
    
    solutions = 0
    
    for denominator in xrange(2, LIMIT + 1):
        for numerator in xrange(int(ceil(float(denominator) / 3)), denominator / 2 + 1):
            
            if numerator == 1 and (denominator == 3 or denominator == 2):
                continue
            
            if gcd(numerator, denominator) == 1:
                solutions += 1
    
    print "Number of reduced, proper fractions between 1/3 and 1/2: ", solutions
    end = time()
    print "Runtime: ", end - start, " seconds."

if __name__ == '__main__':
    main()