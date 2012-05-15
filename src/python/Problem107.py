'''
Created on May 13, 2012

@author: mchrzanowski
'''

import os.path
from time import time

DEFAULT_NUMBER = 1 * 10 ** 7

def readInMatrix(fileName):
    
    matrix = []
    with open(os.path.join(os.curdir, fileName), 'r') as f:
        for line in f:
            newRow = []
            for weight in line.rstrip("\n\r").split(','):
                if not weight.isdigit():
                    newRow.append(DEFAULT_NUMBER)
                else:
                    newRow.append(int(weight))
            matrix.append(newRow)
    
    return matrix

def getTotalEdgeWeightOfMatrix(matrix):
    
    totalEdgeWeight = 0
    
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[i])):
            if matrix[i][j] != DEFAULT_NUMBER:
                totalEdgeWeight += matrix[i][j]
                    
    totalEdgeWeight /= 2
    
    return totalEdgeWeight

def createMST(matrix):
    ''' Prim's algo '''
    
    def connectNewVertexToMST(matrix, mstVertices):
    
        minimumWeightedEdge = DEFAULT_NUMBER
        vertexInMST = None
        vertexJoiningMST = None
        
        for i in mstVertices:
            for j in xrange(len(matrix[i])):
                if j not in mstVertices and matrix[i][j] < minimumWeightedEdge:
                    minimumWeightedEdge = matrix[i][j]
                    vertexInMST = i
                    vertexJoiningMST = j
        
        if vertexJoiningMST is None:
            raise Exception("No new vertex to add to the MST!")
        
        # wipe out this edge from the weight matrix.
        matrix[vertexInMST][vertexJoiningMST] = DEFAULT_NUMBER
        matrix[vertexJoiningMST][vertexInMST] = DEFAULT_NUMBER
        mstVertices.add(vertexJoiningMST)
        
        return minimumWeightedEdge
    
    
    mstVertices = {0}   # start with the 1st vertex by default
    mstEdgeWeight = 0    
    
    # connect a new vertex to our Minimum Spanning Tree.
    # function returns the edge weight used to connect the newest vertex.
    for _ in xrange(len(matrix) - 1):
        mstEdgeWeight += connectNewVertexToMST(matrix, mstVertices)
    
    return mstEdgeWeight
    
def main(): 
    
    # implementation of Prim's algorithm using adjacency lists (ie, a matrix)
    # http://en.wikipedia.org/wiki/Prim%27s_algorithm
    
    # store adjacency lists.
    matrix = readInMatrix('./requiredFiles/Problem107Network.txt')
    
    # get the total weight of the network.
    totalEdgeWeight = getTotalEdgeWeightOfMatrix(matrix)
    
    # get the weight of a minimum spanning tree containing all vertices in the network
    mstEdgeWeight = createMST(matrix)
   
    
    print "Total Edge Weight:", totalEdgeWeight
    print "MST Total Weight:", mstEdgeWeight
    print "Savings from MST Construction:", totalEdgeWeight - mstEdgeWeight
        
if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."
