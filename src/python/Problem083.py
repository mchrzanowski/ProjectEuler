'''
Created on Feb 27, 2012

@author: mchrzanowski
'''
import os.path
from time import time

DUMMY_VALUE = tuple([10 ** 6, [10 ** 6]])


def createMatrix(relativeFilePath):
    file = open(os.path.join(os.curdir, relativeFilePath), 'r')
    matrix = []
    for row in file:
        newRow = [tuple([int(number), []]) for number in row.rstrip("\n").split(",")]
        newRow.insert(0, DUMMY_VALUE)
        newRow.append(DUMMY_VALUE)
        matrix.append(newRow)
        
    # make the zeros and last row/columns be dummy values to avoid special casing
    zeroRow = [DUMMY_VALUE for number in xrange(len(matrix) + 2)]
    
    matrix.insert(0, zeroRow)
    matrix.append(zeroRow)
            
    return matrix, len(matrix) - 2

def updateLocation(currentLocation, touchesFirstBlock, *potentialNewParents):
    
    winnerParent = DUMMY_VALUE
    
    # choose the parent matrix point that has the smallest valid sum.
    for parent in potentialNewParents:
        if parent != DUMMY_VALUE and len(parent[1]) > 0 and (parent[0] + sum(parent[1])) < (winnerParent[0] + sum(winnerParent[1])):
            winnerParent = parent
    
    # now update this point's parent list 
    del currentLocation[1][:]
    currentLocation[1].extend(winnerParent[1])
    
    if not touchesFirstBlock:
        currentLocation[1].append(winnerParent[0])
            
def backwardPropagation(matrix, trueSize, horizonalUpdate, verticalUpdate):
    ''' perform two updates on each matrix chunk: a clockwise and counterclockwise revision. go backwards in chunk layers.
    will again check all 4 matrix points around itself. '''
    for chunk in xrange(trueSize, 0, -1):
        # counter-clockwise revision. check up, left, and if present, down and right
        for column in xrange(1, chunk + 1):
            if chunk == 2 and column == 1: touchesFirstBlock = True     # first block is a special case as it has its number its list.
            else: touchesFirstBlock = False                             
            verticalUpdate(chunk, column, touchesFirstBlock)
        
        for row in xrange(chunk - 1, 0, -1):
            if chunk == 2 and row == 1: touchesFirstBlock = True
            else: touchesFirstBlock = False
            horizonalUpdate(row, chunk, touchesFirstBlock)
        
        # now the clock-wise revision.
        for row in xrange(1, chunk + 1):
            if chunk == 2 and row == 1: touchesFirstBlock = True
            else: touchesFirstBlock = False
            horizonalUpdate(row, chunk, touchesFirstBlock)
        
        for column in xrange(chunk, 0, -1):
            if chunk == 2 and column == 1: touchesFirstBlock = True
            else: touchesFirstBlock = False                             
            verticalUpdate(chunk, column, touchesFirstBlock)


def forwardPropagation(matrix, trueSize, horizonalUpdate, verticalUpdate):
    ''' perform two updates on each matrix chunk: a clockwise and counterclockwise revision. we evaluate chunks going from 
    the top-left to the bottom right
    each check looks for all 4 blocks around it to update itself.'''
    
    for chunk in xrange(2, trueSize + 1):
        # counter-clockwise revision. check up, left, and if present, down and right
        for column in xrange(1, chunk + 1):
            if chunk == 2 and column == 1: touchesFirstBlock = True     # first block is a special case as it has its number its list.
            else: touchesFirstBlock = False                             
            horizonalUpdate(chunk, column, touchesFirstBlock)
        
        for row in xrange(chunk - 1, 0, -1):
            if chunk == 2 and row == 1: touchesFirstBlock = True
            else: touchesFirstBlock = False
            verticalUpdate(row, chunk, touchesFirstBlock)
        
        # now the clock-wise revision.
        for row in xrange(1, chunk + 1):
            if chunk == 2 and row == 1: touchesFirstBlock = True
            else: touchesFirstBlock = False
            verticalUpdate(row, chunk, touchesFirstBlock)
        
        for column in xrange(chunk, 0, -1):
            if chunk == 2 and column == 1: touchesFirstBlock = True     # first block is a special case as it has its number its list.
            else: touchesFirstBlock = False                             
            horizonalUpdate(chunk, column, touchesFirstBlock)


def findSmallestSum(matrix, trueSize):
    ''' the way this is going to work is by dividing the matrix into row/column chunks.
    rowN, colN corresponds to chunk N. for example, chunks on a 3x3 matrix (remember that we append guards to
    our matrix to eliminate edge cases):
    1    2    3
    2    2    3
    3    3    3
    Each matrix location has a tuple of the matrix value and the list of values that led to 
    that point. so we first do a forward propagation on matrix chunks that check each matrix point in that
    chunk in clockwise and counterclockwise directions. 
    we then do a back propagation because, when doing the forward prop, chunks# with # > N weren't filled yet.
    these can be important ways of optimizing the path.
    we then do a final forward prop incorporating the backprop changes. '''
    
    matrix[1][1][1].append(matrix[1][1][0])     # to start it off.
    
    horizonalUpdate = lambda row, column, touchesFirstBlock:                                            \
                    updateLocation(matrix[row][column], touchesFirstBlock, matrix[row][column - 1],     \
                    matrix[row - 1][column], matrix[row][column + 1], matrix[row + 1][column])
    
    verticalUpdate = lambda row, column, touchesFirstBlock:                                             \
                    updateLocation(matrix[row][column], touchesFirstBlock, matrix[row - 1][column],     \
                    matrix[row][column - 1], matrix[row][column + 1], matrix[row + 1][column])
    
    forwardPropagation(matrix, trueSize, horizonalUpdate, verticalUpdate)
    backwardPropagation(matrix, trueSize, horizonalUpdate, verticalUpdate)
    forwardPropagation(matrix, trueSize, horizonalUpdate, verticalUpdate)
    
    return matrix[trueSize][trueSize]
    

def main():
    MATRIX_RELATIVE_FILE_PATH = './requiredFiles/Problem083Matrix.txt'
    matrix, trueSize = createMatrix(MATRIX_RELATIVE_FILE_PATH)
    value, summation =  findSmallestSum(matrix, trueSize)
    
    print "Smallest Sum: ", value + sum(summation)
    

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."