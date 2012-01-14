'''
Created on Jan 9, 2012

@author: mchrzanowski
'''

from time import time

LIMIT = 100

def main():
    start       = time()
    resultSet   = set([])
   
    matrix      = [[0 for j in range(LIMIT + 1)] for i in range(LIMIT + 1)]
    
    createSet(matrix, resultSet)
    end = time()

    print "Size: ", len(resultSet)
    print "Time: ", (end - start), " seconds."
    
def createSet(matrix, resultSet):
    for a in xrange(2, LIMIT + 1):
        for b in xrange(2, LIMIT + 1):
            if matrix[a][b] is 0:
                result = a ** b
                resultSet.add(result)
                matrix[a][b] = 1
    
    
if __name__ == '__main__':
    main()  