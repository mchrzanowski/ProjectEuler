'''
Created on Jan 8, 2012

@author: mchrzanowski
'''

from time import time

totalPaths = 0
END = 21

def main():
# initialization.
    start = time()
    matrix = [[0 for j in xrange(END)] for i in xrange(END)]
    for i in xrange(END):
        matrix[i][0] = matrix[0][i] = 1
   
    findPathsMemoized(matrix)
    print "Total Paths: ", matrix[END-1][END-1]
    end = time()
    print "Runtime: ", end - start, " seconds."


# dynamic programming FTW.
def findPathsMemoized(matrix):
    for i in xrange(1, END):
        for j in xrange(1, END):
            matrix[i][j] =  matrix[i][j-1] +  matrix[i-1][j]


# SO. SLOW. OMG.
def findPaths(i, j):
    if i == END and j == END:
        global totalPaths
        totalPaths = totalPaths + 1
    else:
        if i < END:
            findPaths(i + 1, j)
        if j < END:
            findPaths(i, j + 1)

if __name__ == '__main__':
    main()   