'''
Created on May 7, 2012

@author: mchrzanowski
'''

from time import time

def recurrenceRelation(firstResult, secondResult, thirdResult):
    memoizedDict = {1:firstResult, 2:secondResult, 3:thirdResult}
    iterator = 4
    while True:
        memoizedDict[iterator] = 15 * memoizedDict[iterator - 1] - 15 * memoizedDict[iterator - 2] + memoizedDict[iterator - 3]
        yield memoizedDict[iterator]
        iterator += 1
        
def constructProperPerimeterSolutions(defaultSides, recurrenceRelation, perimeterConstruction, LIMIT):
    solutions = 0
    
    for defaultSide in defaultSides:
        solutions += perimeterConstruction(defaultSide)
        
    for newSide in recurrenceRelation:
        perimeter = perimeterConstruction(newSide)
        if perimeter <= LIMIT:
            solutions += perimeter
        else:
            break
        
    return solutions
    

def main():
    
    # recurrence relationships received from:
    # http://www.had2know.com/academics/nearly-equilateral-heronian-triangles.html
    
    LIMIT = 1 * 10 ** 9
    solutions = 0

    # first, calculate the n, n, n+1 heronian isosceles triangles.
    # seed the recurrence relation method with the first 3 n I found by hand that 
    # create valid triangles   
    defaultNNNPlusOneSides = (5, 65, 901) 
    nNNPlusOne = recurrenceRelation(*defaultNNNPlusOneSides)
    createPerimeterForNNNPlusOne = lambda x: x * 3 + 1
    
    solutions += constructProperPerimeterSolutions(defaultNNNPlusOneSides, nNNPlusOne, createPerimeterForNNNPlusOne, LIMIT)
    
    # now, calculate the n, n, n-1 triangles.
    defaultNNNMinusOneSides = (17, 241, 3361)
    nNNMinusOne = recurrenceRelation(*defaultNNNMinusOneSides)
    createPerimeterForNNNMinusOne = lambda x: x * 3 - 1   
    
    solutions += constructProperPerimeterSolutions(defaultNNNMinusOneSides, nNNMinusOne, createPerimeterForNNNMinusOne, LIMIT)
    
    print "Solutions:", solutions    
        

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."