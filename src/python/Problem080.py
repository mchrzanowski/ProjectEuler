'''
Created on Feb 17, 2012

@author: mchrzanowski
'''

from decimal import getcontext, Decimal
from math import floor, sqrt
from time import time


LIMIT = 10 ** 2

def sumUpDigits(number):
    
    getcontext().prec = LIMIT + len(str(int(sqrt(LIMIT))))
    
    root = Decimal(number).sqrt()
    
    if root // 1 == root:
        return 0
    
    sumOfDigits = int(root)
    
    root -= int(root)    
    
    for digit in str(root)[2 : LIMIT + 1]:
        sumOfDigits += int(digit)
        
    return sumOfDigits
    

def main():
    start = time()
    sum = 0
    for i in xrange(1, LIMIT + 1):
        sum += sumUpDigits(i)
    
    print "Sum of first 100 digits in irrational sqrts of numbers <=", LIMIT, " : ", sum
    
    end = time()
    print "Runtime: ", end - start, " seconds."

if __name__ == '__main__':
    main()