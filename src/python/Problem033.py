'''
Created on Jan 16, 2012

@author: mchrzanowski
'''

import sys
from time import time
from fractions import gcd

def findInterestingFractions(LIMIT):
    possibilities = set([])

    for numerator in xrange(10, LIMIT):
        for denominator in xrange(numerator + 1, LIMIT):
            
            currentResult = float(numerator) / denominator
            
            numeratorSet = set([int(character) for character in str(numerator)])
            denominatorSet = set([int(character) for character in str(denominator)])
            
            if len(numeratorSet) is not 2 or len(denominatorSet) is not 2:
                continue        # each number should have two different numbers.
            
            if 0 in numeratorSet or 0 in denominatorSet:
                continue        # eliminate trivial cases where each number possesses a zero.
            
            newNumeratorSet = numeratorSet - denominatorSet
            newDenominatorSet = denominatorSet - numeratorSet
            
            if len(newNumeratorSet) is not 1 or len(newDenominatorSet) is not 1:
                continue        # each 2-digit number should now be reduced to 1 digit. 
                        
            newNumerator = newNumeratorSet.pop()
            newDenominator = newDenominatorSet.pop()
            
            newResult = float(newNumerator) / newDenominator
            
            if abs(currentResult - newResult) <= sys.float_info.epsilon:
                possibilities.add(tuple([numerator, denominator]))
                
    return possibilities


def main():
    
    LIMIT = 100
    
    start = time()
    possibilities = findInterestingFractions(LIMIT)
    
    resultingNumerator = 1
    resultingDenominator = 1
    
    for pair in possibilities:
        resultingNumerator *= pair[0]
        resultingDenominator *= pair[1]
    
    divisorToUse = gcd(resultingNumerator, resultingDenominator)
    
    resultingProduct = float(resultingNumerator / divisorToUse) / (resultingDenominator / divisorToUse)
    
    end = time()
    print "Product: ", resultingProduct  
    print "Runtime: ", end - start, " seconds. "  
           
        
if __name__ == '__main__':
    main()