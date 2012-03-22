'''
Created on Mar 20, 2012

@author: mchrzanowski
'''

from time import time

def getNumberOfAdditionPossibilities(n):
    ways = 2    # by default, we can include (1 / n / 2) * 2 and (1 / (n + 1)) + something.
    for i in xrange(n + 2, 2 * n):
        if (float(n * i) / (n - i)).is_integer():
            ways += 1
    return ways

def main():
    
    LIMIT = 10 ** 3
    solution = 0
    iteration = 2
        
    while solution == 0:
        
        if getNumberOfAdditionPossibilities(iteration) >= LIMIT:
            solution = iteration
        
        iteration += 1
        
#        if iteration % 1000 == 0: 
#            print iteration
        
    print "Solution: ", solution

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."
