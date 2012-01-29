'''
Created on Jan 26, 2012

@author: mchrzanowski
'''

from ProjectEulerPrime import ProjectEulerPrime
from time import time

PRIME_FAMILY_CARDINALITY = 8
ELEVENTH_BASE = 'X'


def substitueAndCheckPrimality(primeObject, sequence):
    
    if ELEVENTH_BASE not in sequence:
        return False
    
    failures = 0
    primesFound = 0
    for i in xrange(10):
        if i == 0 and sequence[0] == ELEVENTH_BASE:
            continue
        if not primeObject.isPrime(str.replace(sequence, ELEVENTH_BASE, str(i))):
            failures += 1
            if failures >= 2:       # of at most 10 iterations, no more than 2 can fail to produce primes.
                return False
        else:
            primesFound += 1
    
    if primesFound == PRIME_FAMILY_CARDINALITY:
        return True
    else: 
        return False
    
def base11Increment(sequence, valueToCheck = -1):
    ''' 
        we define our number set to be 0123456789X
        take a sequence of characters and increment using our special 
        base.
    '''
    if abs(valueToCheck) > len(sequence):
        return sequence.insert(0, '1')
        
    if sequence[valueToCheck] == ELEVENTH_BASE:   # carry time.
        sequence[valueToCheck] = '0'
        return base11Increment(sequence, valueToCheck - 1)
        
    elif sequence[valueToCheck] == '9':
        sequence[valueToCheck] = ELEVENTH_BASE
        return
    else:
       sequence[valueToCheck] = chr(ord(sequence[valueToCheck]) + 1)
       return
    
def main():
    '''
        To solve this problem, I use base-11 numbers instead of base-10; X is my 11th base.
        I swap X characters to create prime numbers in base 10.
    '''
    start = time()
    primeObject = ProjectEulerPrime()
    solution = 0
    candidateList = [char for char in '56XX5']      # has to be at least greater than the template for the smallest 7-member prime family 
    while solution == 0:                            # and odd, obviously.
        
        if substitueAndCheckPrimality(primeObject, "".join(candidateList)):
            solution = "".join(candidateList)
        
        base11Increment(candidateList)
        base11Increment(candidateList)  # increment by 2 to keep number odd.
               
    print "8-digit prime family template: ", solution                       
    end = time()
    print "Runtime: ", end - start, " seconds."

if __name__ == '__main__':
    main()