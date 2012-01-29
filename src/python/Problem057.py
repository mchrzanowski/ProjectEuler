'''
Created on Jan 29, 2012

@author: mchrzanowski
'''

from time import time

LIMIT = 1000
BASE = 2

def findLargerDigitExpansions():
    numeratorDict           = {}
    denominatorDict         = {}
    
#default cases.
    numeratorDict[-1]       = 1
    denominatorDict[-1]     = 0
    numeratorDict[0]        = 1
    denominatorDict[0]      = 1
    
#    formula (thanks, Wikipedia!):
#    numerator   = BASE * previousNumerator + previousPreviousNumerator
#    same for denominator.
    
    solutions = 0
        
    for expansion in xrange(1, LIMIT):
        numeratorDict[expansion] = BASE * numeratorDict[expansion - 1] + numeratorDict[expansion - 2]
        denominatorDict[expansion] = BASE * denominatorDict[expansion - 1] + denominatorDict[expansion - 2]
            
        if len(str(numeratorDict[expansion])) > len(str(denominatorDict[expansion])):
            solutions += 1
   
    return solutions

def main():
    
    start = time()
    print "Solutions: ", findLargerDigitExpansions()
    end = time()
    print "Runtime: ", end - start, " seconds."
    
if __name__ == '__main__':
    main()