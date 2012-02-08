'''
Created on Feb 7, 2012

@author: mchrzanowski
'''
from time import time

def findRationalApproximation(quotients):
    numeratorDict           = {}
    denominatorDict         = {}
    
    #default cases.
    numeratorDict[-1]       = 1
    denominatorDict[-1]     = 0
    
    numeratorDict[0]        = quotients[0]
    denominatorDict[0]      = 1
    
#    formula (thanks, Wikipedia!):
#    numerator   = quotient * previousNumerator + previousPreviousNumerator
#    same for denominator.
    
    for expansion in xrange(1, len(quotients)):
        numeratorDict[expansion] = quotients[expansion] * numeratorDict[expansion - 1] + numeratorDict[expansion - 2]
        denominatorDict[expansion] = quotients[expansion] * denominatorDict[expansion - 1] + denominatorDict[expansion - 2]
    
    return tuple([numeratorDict[len(quotients) - 1], denominatorDict[len(quotients) - 1]])

LIMIT = 100
def main():
    
    start = time()
    # first, we find the first LIMIT or so quotients of e
    # we follow the pattern of e's expansion from Wikipedia. 
    
    eQuotientList = [2, 1, 2]
    for i in xrange(LIMIT / 3):
        eQuotientList.append(1)
        eQuotientList.append(1)
        eQuotientList.append(eQuotientList[-3] + 2)
    
    # then, we use the continued fraction formula that we used in problem 57
    rationalApproximation = findRationalApproximation(eQuotientList[:LIMIT])
    
    print "We got: ", rationalApproximation
    print "Sum of digits of the 100th rational approximation's numerator: ", sum([int(char) for char in str(rationalApproximation[0])])
    end = time()
    print "Runtime: ", end - start, " seconds."
    
    
if __name__ == '__main__':
    main()