'''
Created on Feb 19, 2012

@author: mchrzanowski
'''
from ProjectEulerLibrary import phi
from time import time

DIGITS_TO_SEE = 8
LIMIT = 10 ** DIGITS_TO_SEE

def main():
    
    start = time()
    
    A = 1777
    B = 1855
    
    phiLimit = phi(LIMIT)
    
    '''
    we use efficient modular exponentiation to do this.
    essentially, there are several highly efficient ways 
    of computing (a ^ b) mod n. Python just so happens to use 
    binary exponentiation in its built-in pow() function.
    http://en.wikipedia.org/wiki/Modular_exponentiation
    
    we also use Euler's theorem:
    http://en.wikipedia.org/wiki/Euler's_theorem
    '''
    residual = A
    for i in xrange(B - 2): residual = pow(A, residual, phiLimit) 
    residual = pow(A, residual, LIMIT)
    
    print "Last ", DIGITS_TO_SEE, " digits from the tetration (", A, ", ", B, "): ", residual
    end = time()
    print "Runtime: ", end - start, " seconds."

if __name__ == '__main__':
    main()