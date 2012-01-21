'''
Created on Jan 21, 2012

@author: mchrzanowski
'''

from time import time
from ProjectEuler import isPrime

SOLUTION_LIMIT = 11     # we know there to only exist 11 circularly-truncatable primes
SINGLE_DIGIT_PRIME_SET = set(['2','3','5','7'])     # list of single-digit primes.
DOUBLE_DIGIT_PRIME_SET = set(['23','29','31','37','41','43','47','53','59','61','67','71','73','79'])   #relevant 2-digit primes.

def produceNumbersFromRightTruncation(number):
    number = str(number)
    for i in xrange(1, len(number)):
        yield int(number[:i])

def produceNumbersFromLeftTruncation(number):
    number = str(number)
    for i in xrange(1, len(number)):
        yield int(number[i:])
        
def checkCandidateWorthiness(number):
    if '0' in number:
        return False
    if number[-1] not in SINGLE_DIGIT_PRIME_SET:
        return False
    if number[0] not in SINGLE_DIGIT_PRIME_SET:
        return False
    if number[:2] not in DOUBLE_DIGIT_PRIME_SET:
        return False
    if not isPrime(number):
        return False
    return True

def main():
    
    start = time()
   
    primeSet    = set([])
    solutionSet = set([])
    candidate   = str(11)           # skip 2,3,5,7 as per the question.
    
    while len(solutionSet) != SOLUTION_LIMIT:
                
        if checkCandidateWorthiness(candidate):
            
            
            isPrimeFromLeftTruncation = True
            
            for number in produceNumbersFromLeftTruncation(candidate):
                if number not in primeSet:
                    if isPrime(number):
                        primeSet.add(number)
                    else:
                        isPrimeFromLeftTruncation = False
                        break
            
            isPrimeFromRightTruncation = True
    
            if isPrimeFromLeftTruncation:
                for number in produceNumbersFromRightTruncation(candidate):
                    if number not in primeSet:
                        if isPrime(number):
                            primeSet.add(number)
                        else:
                            isPrimeFromRightTruncation = False
                            break
            
            if isPrimeFromLeftTruncation and isPrimeFromRightTruncation:
                solutionSet.add(int(candidate))
                
        candidate = str(int(candidate) + 1)
        
    end = time()
    
    print "Solutions: ", solutionSet
    print "Sum: ", sum(solutionSet)
    print "Runtime: ", end - start, " seconds."
    

if __name__ == '__main__':
    main()