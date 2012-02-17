'''
Created on Feb 16, 2012

@author: mchrzanowski
'''

from decimal import getcontext, Decimal
from math import floor, sqrt
from time import time

LIMIT = 10 ** 4

# ericn's solution from the project euler forums (http://projecteuler.net/thread=64;page=5)
# is much, much more efficient than mine.
def hasOddPeriod(number):
    
    root = sqrt(number)
    
    if root.is_integer():
        return False
    
    quotients = -1
    
    numbersSeen = set()
    
    # defaults
    sqrtSubtractor, denominator, newQuotient = 0, 1, int(root)
    
    state = sqrtSubtractor, denominator, newQuotient
    
    while state not in numbersSeen:
        
        numbersSeen.add(state)
        
        quotients += 1
        
        sqrtSubtractor = denominator * newQuotient - sqrtSubtractor
        
        denominator = (number - sqrtSubtractor ** 2) / denominator
        
        newQuotient = (int(root) + sqrtSubtractor) / denominator
        
        state = sqrtSubtractor, denominator, newQuotient
        
    if quotients & 1 == 1:
        return True
    
    return False

# my method. REALLY slow because of the floating number precision required.
# algo derived from:
# http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/cfINTRO.html#sqrtalgsalg
def old_hasOddPeriod(number):
    
    sqrtOfNumber = number ** 0.5
    
    if sqrtOfNumber.is_integer():
        return False
    
    getcontext().prec = 250
    sqrtOfNumber = Decimal(number).sqrt()
    
    initialResidual = round(sqrtOfNumber + int(sqrtOfNumber), 1)
    
    currentResidual = sqrtOfNumber
    
    quotientNumber = 0    
    
    while round(currentResidual, 1) != initialResidual:
        
        intCurrentResidual = int(currentResidual)
        
        currentResidual = (currentResidual - intCurrentResidual) ** -1
                
        quotientNumber += 1 
        
    if quotientNumber & 1 == 1:
        return True
    
    return False

def main():
    start = time()
    oddPeriods = 0
    for i in xrange(1, LIMIT + 1):
        if hasOddPeriod(i):
            oddPeriods += 1
            
    print "Number of continued fractions with odd periods: ", oddPeriods
    end = time()
    print "Runtime: ", end - start, " seconds."
    

if __name__ == '__main__':
    main()