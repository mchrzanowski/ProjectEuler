'''
Created on Jan 21, 2012

@author: mchrzanowski
'''

from ProjectEulerLibrary import generateTriangleNumbers, generateHexagonalNumbers, generatePentagonalNumbers

from time import time

LIMIT = 400                         # found through trial and error

STARTING_PENTAGONAL_NUMBER  = 165    # based on the problem
STARTING_TRIANGLE_NUMBER    = 285
STARTING_HEXAGONAL_NUMBER   = 143

def main():
    
    start = time()
    triangleSet = set([number for number in generateTriangleNumbers(LIMIT, STARTING_TRIANGLE_NUMBER)])
    hexagonalSet = set([number for number in generateHexagonalNumbers(LIMIT, STARTING_HEXAGONAL_NUMBER)])
    
    for number in generatePentagonalNumbers(LIMIT, STARTING_PENTAGONAL_NUMBER):
        if number in triangleSet and number in hexagonalSet:
            solution = number
            break
    
    print "Next Number: ", solution
            
    end = time()
    print "Runtime: ", end - start, " seconds. "

if __name__ == '__main__':
    main()