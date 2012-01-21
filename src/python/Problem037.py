'''
Created on Jan 21, 2012

@author: mchrzanowski
'''

from time import time
from ProjectEulerConstants import isPrime

SOLUTION_LIMIT = 11

def produceNumbersFromRightTruncation(number):
    number = str(number)
    for i in xrange(1, len(number)):
        yield int(number[:i])

def produceNumbersFromLeftTruncation(number):
    number = str(number)
    for i in xrange(1, len(number)):
        yield int(number[i:])

def main():
    
    start = time()
   
    primeSet = set([])
    solutionSet = set([])
    candidate = 11           # skip 2,3,5,7 as per the question.
    
    while len(solutionSet) != 11:
                
        if isPrime(candidate):
            
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
                solutionSet.add(candidate)
                
        candidate += 1
        
    end = time()
    
    print "Solutions: ", solutionSet
    print "Sum: ", sum(solutionSet)
    print "Runtime: ", end - start, " seconds."
    

if __name__ == '__main__':
    main()