'''
Created on Jan 8, 2012

@author: mchrzanowski
'''

totalPaths = 0
END = 21

def main():
# initialization.
    matrix = [[0 for j in range(END)] for i in range(END)]
    for i in range(END):
        matrix[i][0] = matrix[0][i] = 1
   
    findPathsMemoized(matrix)
    print "Total Paths: ", matrix[END-1][END-1]


# dynamic programming FTW.
def findPathsMemoized(matrix):
    for i in range(1, END):
        for j in range(1, END):
            accumulator = matrix[i-1][j]
            if j - 1 >= 0:
                accumulator = accumulator + matrix[i][j-1]
            matrix[i][j] = accumulator


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