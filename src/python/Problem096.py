'''
Created on Mar 4, 2012

@author: mchrzanowski
'''

import os.path
import re
from time import time

DEFAULT = 0

def readInMatrices(fileName):
    matrixCollection = []
    newMatrixPattern = re.compile("Grid [0-9]+")
    file = open(os.path.join(os.curdir, fileName), 'r')
    for line in file:
        line = line.rstrip("\n")
        if newMatrixPattern.match(line):
            matrixCollection.append([])
        else:
            matrixCollection[-1].append([int(number) for number in line])
            
    return matrixCollection

def copyMatrix(matrixToCopy):
    ''' deep copy of a matrix '''
    newMatrix = []
    for row in xrange(len(matrixToCopy)):
        newMatrix.append(list(matrixToCopy[row]))
    return newMatrix

def isColumnStillUnique(colToCheck, matrix):
    ''' check a row for non-DEFAULT duplicates '''
    seen = set([])
    for row in xrange(len(matrix)):
        if matrix[row][colToCheck] not in seen:
            seen.add(matrix[row][colToCheck])
        elif matrix[row][colToCheck] != DEFAULT:
            return False
    
    return True

def isBoxStillUnique(boxToCheck, matrix):
    ''' box check for non-DEFAULT duplicates '''
    startRow, startColumn = getMatrixStartPoints(boxToCheck)
    seen = set([])
    for row in xrange(startRow, startRow + 3):
        for col in xrange(startColumn, startColumn + 3):
            if matrix[row][col] not in seen:
                seen.add(matrix[row][col])
            elif matrix[row][col] != DEFAULT:
                return False
    return True
    

def isRowStillUnique(rowToCheck, matrix):
    ''' check if a given row contains no duplicates except the DEFAULT case '''
    seen = set([])
    
    for number in matrix[rowToCheck]:
        if number not in seen:
            seen.add(number)
        elif number != DEFAULT:
            return False
    
    return True

def getMatrixStartPoints(boxNumber):
    ''' return the top-left i,j location of a given box'''
    return 3 * int(boxNumber / 3), 3 * (boxNumber % 3)
    
def getBoxNumber(row, column):
    ''' return the box number corresponding to a given row, column matrix point '''
    return 3 * int(row / 3) + int(column / 3)

def solveSudoku(matrix):
    ''' depth-first, backtracking algorithm. variant of Ariadne's Thread:
    http://www.sudopedia.org/wiki/Ariadne's_Thread
    '''
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix)):
            if matrix[i][j] == DEFAULT:
                for newNumber in xrange(1, 10):
                    
                    matrix[i][j] = newNumber
                    
                    if isRowStillUnique(i, matrix) and           \
                    isColumnStillUnique(j, matrix) and           \
                    isBoxStillUnique(getBoxNumber(i, j), matrix):
                        
                        newMatrix = copyMatrix(matrix)
                        returnValue = solveSudoku(newMatrix)
                        
                        if returnValue is not False:
                            return returnValue
                
                return False
    
    return matrix        
         
def main():
    matrixCollection = readInMatrices('./requiredFiles/Problem096Matrices.txt')
    topOfMatrices = []
    for matrix in matrixCollection:
        solvedMatrix = solveSudoku(matrix)
        topOfMatrices.append(int(''.join([str(number) for number in solvedMatrix[0][0:3]])))
    
    print "Solution:", sum(topOfMatrices)

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."