'''
Created on Feb 18, 2012

@author: mchrzanowski
'''
from math import log
import os.path
from time import time

def main():
    ''' just compare the logs of the numbers.'''
    start = time()
    
    numbersFile = open(os.path.join(os.curdir,'./requiredFiles/Problem099Numbers.txt'), 'r')
    
    row = 0
    maxRow = 0
    maxNumber = 0
    # numbers come in rows as : base, exp 
    for line in numbersFile:
        row += 1
        base, exponent = [int(number) for number in line.strip().split(",")]
        if exponent * log(base) > maxNumber:
            maxNumber = exponent * log(base)
            maxRow = row
        
    
    print "Row with max value: ", maxRow
    end = time()
    print "Runtime: ", end - start, " seconds."
       

if __name__ == '__main__':
    main()