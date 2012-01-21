'''
Created on Jan 20, 2012

@author: mchrzanowski
'''

from ProjectEulerConstants import isNumberPandigital
from time import time
from math import ceil

LIMIT = 9999        # as a ceiling, since any candidate must be multiplied by at least 2 and 
                    # hence must at least double its length for the first one concatenation operation, 
                    # the limit must be at most 4 digits ( 4 + 4 = 8)
LENGTH_LIMIT = 9    # [1-9] pandigital number

def main():
    start = time()
    maxNumber = 0
    for i in xrange(2, LIMIT):
        numberString = str(i)
        for multiplier in xrange(2, int(ceil(float(LENGTH_LIMIT) / (2 * len(str(i))))) + 1):    # candidate must at least fit 2 numbers.
            numberString += str(i * multiplier)
            
            if len(numberString) > LENGTH_LIMIT:
                break
            
            elif len(numberString) == LENGTH_LIMIT and isNumberPandigital(numberString):
                    if int(numberString) > maxNumber:
                       maxNumber = int(numberString)
    
    print "Max pandigital number constructed this way: ", maxNumber                   
    end = time()
    print "Runtime: ", end - start, " seconds."
    
if __name__ == '__main__':
    main()