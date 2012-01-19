'''
Created on Jan 16, 2012

@author: mchrzanowski
'''

from math import factorial
from time import time

LIMIT = 2540160     # upper bound : 7 * 9! . this is because 9^7 is 4782969
                    # and there is no way to go from factorial sums to the actual number 
                    # after this ceiling. 

def main():
    start = time()
    solutions = set([])
    
    factorialMap = {}
    for i in xrange(0, 10):
        factorialMap[str(i)] = factorial(i)
            
    for i in xrange(10, LIMIT + 1):
        value = 0    
        for char in str(i):  
            value += factorialMap[char]
        if value == i:
            solutions.add(i)
    
    print "Solution: ", sum(solutions)
    end = time()
    print "Runtime: ", end - start, " seconds."

    
if __name__ == '__main__':
    main()
