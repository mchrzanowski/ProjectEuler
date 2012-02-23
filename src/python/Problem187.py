'''
Created on Feb 21, 2012

@author: mchrzanowski
'''
from ProjectEulerPrime import ProjectEulerPrime
from math import sqrt
from time import time

LIMIT = 10 ** 8

''' naive implementation of the prime counting function'''
def pi(number, storedList=[]):
            
    if len(storedList) < number:
        
        del storedList[:]
        
        storedList.extend([0 for number in xrange(number + 1)])
    
        storedList[0] = storedList[1] = 1
    
        for i in xrange(2, int(sqrt(number)) + 1):
            if storedList[i] == 1: continue
            currentValue = i + i
            while currentValue < len(storedList):
                storedList[currentValue] = 1
                currentValue += i
        
    return len([storedList[number] for number in xrange(number + 1) if storedList[number] == 0])
    

def main():
    '''
    formula given by MathWorld:
    http://mathworld.wolfram.com/Semiprime.html
    '''

    primeObject = ProjectEulerPrime()
    
    # first, get all primes < sqrt(LIMIT). place a 0 at index 0 for easier indexing.
    primesFound = [0, 2]
    for i in xrange(3, int(sqrt(LIMIT)) + 1, 2):
        if primeObject.isPrime(i):
            primesFound.append(i)
    
    solution = 0
    for i in xrange(1, len(primesFound)): solution += pi(LIMIT / primesFound[i]) - i + 1 
            
    print "Found:", solution, "composites formed from 2 primes."
                
    
if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime: ", end - start, " seconds."