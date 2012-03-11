'''
Created on Mar 8, 2012

@author: mchrzanowski
'''

from Problem066 import getConvergentPair
from decimal import Decimal
from time import time

def getPositiveRoot(x):
    ''' get the positive root of the second-order diophantine equation
    x ** 2 - x - y ** 2 + y - 2 * x * y = 0
    where x is given.
    '''
    x = Decimal(x)  # for sqrt precision.
    
    b = 2 * x - 1
    
    c = -1 * (x ** 2 - x)
    
    return (-b + (b ** 2 - 4 * c).sqrt()) / 2
    

def main():
    ''' 
    the problem is asking for solutions to the Pell equation
    x ** 2 - 2 * y ** 2 = -1
    where:
     x = the number of blue discs
     y = the number of non-blue discs
    find the first x for which x + y > 10 ** 12
    Algo from:
    http://www.johnsasser.com/pdf/article15.pdf
    '''
    
    IRRATIONAL_NUMBER = 2
    LIMIT = 10 ** 12
    
    solution = 0
    
    convergentFunction = getConvergentPair(IRRATIONAL_NUMBER, -1)
        
    while solution == 0:
        numerator, denominator = convergentFunction.next()
        x = (denominator + 1) / 2
        
        y = getPositiveRoot(x)
        
        if x + y > LIMIT:
            solution = x
    
    print "Solution:", solution

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."