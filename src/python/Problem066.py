'''
Created on Feb 21, 2012

@author: mchrzanowski
'''

from math import sqrt
from Problem064 import getQuotients
from Problem065 import findRationalApproximation
from time import time

LIMIT = 10 ** 3



def main():
    ''' here we use two methods from previous problems:
    Problem064 dealt with getting the list of quotients for use in the continued fraction
    Problem065 then dealt with constructing the continued fraction from these quotients
    '''
    start = time()
    
    maxD = 0
    maxX = 0
    
    for i in xrange(1, LIMIT + 1):
        
        if sqrt(i).is_integer(): continue   # skip perfect squares.
        
        quotientList = getQuotients(i)      # get the quotient list. this method will only return up to one full period. 
                                            # we might need more to get convergence, though.
        hasNotConvergedYet = True
        
        while hasNotConvergedYet:
        
            quotientList.extend(quotientList[1:])       # here, we just double the number of periods in the list. The first value is the integer portion.
            
            numerators, denominators = findRationalApproximation(quotientList)  # indexed numerator, denominator dicts
            
            for j in xrange(len(numerators) - 1):   # these dicts are weirdly indexed; they begin at -1.
                
                if numerators[j] ** 2 - i * denominators[j] ** 2 == 1:
                                        
                    if numerators[j] > maxX:
                        maxX = numerators[j]
                        maxD = i
                        
                    hasNotConvergedYet = False
                    break
    
    print "D <=", LIMIT, "that maximizes x:", maxD
    
    end = time()
    print "Runtime: ", end - start, " seconds."

if __name__ == '__main__':
    main()