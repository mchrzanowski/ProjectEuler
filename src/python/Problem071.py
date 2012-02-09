'''
Created on Feb 8, 2012

@author: mchrzanowski
'''

from fractions import Fraction
from time import time

LIMIT = 1000000

def main():
    
    start = time()
   
    highestFraction = Fraction(0, 1)
    ceiling = Fraction(3, 7)
    
    solutionSet = set([])
    
    for denominator in xrange(1, LIMIT + 1):
        for numerator in xrange(3 * denominator / 7, 3 * denominator / 7 + 1):
            newFraction = Fraction(numerator, denominator)
            if newFraction != ceiling and newFraction > highestFraction:
                highestFraction = newFraction
                
        
    print "Closest Proper Fraction < 3/7 : ", highestFraction
    end = time()
    print "Runtime: ", end - start, " seconds."
    
    

if __name__ == '__main__':
    main()
    
    