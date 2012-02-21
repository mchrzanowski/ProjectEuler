'''
Created on Feb 20, 2012

@author: mchrzanowski
'''

from ProjectEulerLibrary import phi
from time import time

def main():
    
    start = time()
    
    solution = 0
    LOOP_LIMIT = 6
    MOD_LIMIT = 14 ** 8
    PHI_LIMIT = phi(MOD_LIMIT)
    
    powDict = {}
    
    for i in xrange(LOOP_LIMIT + 1): 
        newSolution = ackermann(i, MOD_LIMIT, PHI_LIMIT, powDict)
        print i, " : ", newSolution
        solution += newSolution
    
    print "Solution: ", solution % MOD_LIMIT
    
    end = time()
    print "Runtime: ", end - start, " seconds."

def tetration(A, B, modulus, powDict):
    
    # tetration. 2 knuth arrows.
    residual = A
    
    for i in xrange(B - 1):
        if residual not in powDict:
            newResidual = pow(A, residual, modulus)
            powDict[residual] = newResidual
            residual = newResidual
        else:
            residual = powDict[residual] 
    
    return residual

def pentation(A, B, modulo, phiModulo, powDict):
    
    # pentation. 3 arrows.
    powerTower = tetration(A, B - 1, phiModulo, powDict)
    
    residual = A
    for j in xrange(powerTower - 2): 
        if residual not in powDict:
            newResidual = pow(A, residual, phiModulo)
            powDict[residual] = newResidual
            residual = newResidual
        else:
            residual = powDict[residual] 
    
    return residual

def ackermann(number, modulo, phiModulo, powDict):
    
    A = 2

    # algos given by:
    # http://en.wikipedia.org/wiki/Ackermann_function#Table_of_values
    if number == 0:
        return number + 1

    elif number == 1:
        return number + 2

    elif number == 2:
        return A * number + 3

    # from here on out, we use this algo:
    # A(m, n) = 2 knuth_arrow(m-2) (n + 3) - 3
    elif number == 3:
        # exponentiation. 1 knuth arrow.
        return pow(A, number + 3, modulo) - 3

    elif number == 4:
        
        residual = tetration(A, number + 2, phiModulo, powDict)
        return pow(A, residual, modulo) - 3
    
    elif number == 5:
        
        residual =  pentation(A, number + 3, modulo, phiModulo, powDict)
        return pow(A, residual, modulo) - 3
                
    elif number == 6:
                
        # heptation. 4 (omg..) knuth arrows.
        powerTower = pentation(A, number + 3, modulo, phiModulo, powDict)
                
        residual = A
        
        for i in xrange(powerTower - 3): 
            if residual not in powDict:
                newResidual = pow(A, residual, phiModulo)
                powDict[residual] = newResidual
                residual = newResidual
            else:
                residual = powDict[residual]
        
        return pow(A, residual, modulo) - 3
    
    else:
        raise Exception("Number not supported!")

if __name__ == '__main__':
    main()