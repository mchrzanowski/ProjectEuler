'''
Created on Jan 11, 2012

@author: mchrzanowski
'''
import os.path
from time import time


LIMIT = 100

def createWeightMatrix(triangle):
    weights  = [[0 for j in xrange(LIMIT)] for i in xrange(LIMIT)]
    i = 0
    for line in triangle:
        line = line.strip("\n")
        numberList = line.split(" ")
        j = 0
        for number in numberList:
            weights[i][j] = int(number)
            j = j + 1
        i = i + 1
    return weights

def calculateLargestSum(weights):

    for i in xrange(1, LIMIT):
        for j in xrange(LIMIT):
            weights[i][j] = max(weights[i-1][j], weights[i-1][j-1]) + weights[i][j]
    findLargestSum(weights)

def findLargestSum(matrix):   
    maximum = 0
    for j in xrange(LIMIT):
        if matrix[LIMIT - 1][j] > maximum:
            maximum = matrix[LIMIT - 1][j] 
    print "Largest Sum: ", maximum


def main():
    
    begin = time()
    
    triangle = open(os.path.join(os.curdir,'Problem067Triangle.txt'), 'r')
    weights = createWeightMatrix(triangle)
    calculateLargestSum(weights)
    
    end = time()
    print "Runtime: ", (end - begin), " seconds."
    

if __name__ == '__main__':
    main()