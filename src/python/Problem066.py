'''
Created on Feb 21, 2012

@author: mchrzanowski
'''

from math import sqrt
from Problem064 import getQuotients
from Problem065 import findRationalApproximation
from time import time

LIMIT = 10 ** 3


def getConvergentPair(i, difference=1):
    ''' a generator that will return iterations of increasingly-precise numerator,denominator tuples
    of sqrt(i) '''
    quotientList = getQuotients(i)      # get the quotient list. this method will only return up to one full period. 
                                        # we might need more to get convergence, though.
    
    convergentState = 0                 # expansion of the quotient list causes some state to be reset.
                                        # save state because we don't want to send convergents that we've already sent     
    while True:
    
        quotientList.extend(quotientList[1:])       # here, we just double the number of periods in the list. The first value is the integer portion.
        
        numerators, denominators = findRationalApproximation(quotientList)  # indexed numerator, denominator dicts
        
        for j in xrange(convergentState, len(numerators) - 1):   # these dicts are weirdly indexed; they begin at -1.
            
            if numerators[j] ** 2 - i * denominators[j] ** 2 == difference:
                yield numerators[j], denominators[j]
                convergentState = j + 1

def main():
    ''' 
    http://en.wikipedia.org/wiki/Pell's_equation
    
    here we use two methods from previous problems:
    Problem064 dealt with getting the list of quotients for use in the continued fraction
    Problem065 then dealt with constructing the continued fraction from these quotients
    '''
    start = time()
    
    maxD = 0
    maxX = 0
    
    for i in xrange(1, LIMIT + 1):
        
        if sqrt(i).is_integer(): continue   # skip perfect squares.
        
        numerator, denominator = getConvergentPair(i).next()    # first pair will do as we want minimal solutions.
                            
        if numerator > maxX:
            maxX = numerator
            maxD = i
                

    print "D <=", LIMIT, "that maximizes x:", maxD
    
    end = time()
    print "Runtime: ", end - start, " seconds."

if __name__ == '__main__':
    main()