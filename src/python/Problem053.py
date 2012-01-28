'''
Created on Jan 27, 2012

@author: mchrzanowski
'''
from time import time

LIMIT = 101
NUMBER_LIMIT = 1000000

def main():
    
    start = time()
    matrix = [[0 for j in xrange(LIMIT + 1)] for i in xrange(LIMIT + 1)]
    
    solutions = 0
    
    # Pascal's triangle.
    for i in xrange(1, LIMIT + 1):
        matrix[i][1] = 1
        for j in xrange(2, i + 1):
            matrix[i][j] = matrix[i - 1][j] + matrix[i - 1][j - 1]
            if matrix[i][j] > NUMBER_LIMIT:
                solutions += 1
               
    print "Number of values > ", NUMBER_LIMIT, ": " , solutions
    end = time()
    print "Runtime: ", end - start, " seconds. "
    

if __name__ == '__main__':
    main()