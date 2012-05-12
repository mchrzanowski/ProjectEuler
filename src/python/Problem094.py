'''
Created on May 7, 2012

@author: mchrzanowski
'''

from time import time
        
def constructValidHeronianTriangles(perimeterConstruction, LIMIT, firstDefaultSide, secondDefaultSide, thirdDefaultSide):
    
    def getNextSideOfHeronianTriangle(firstResult, secondResult, thirdResult):
        memoization = {1:firstResult, 2:secondResult, 3:thirdResult}
        iterator = 4
        while True:
            memoization[iterator] = 15 * memoization[iterator - 1] - 15 * memoization[iterator - 2] + memoization[iterator - 3]
            yield memoization[iterator]
            iterator += 1
        
    solutions = 0
    
    for defaultSide in (firstDefaultSide, secondDefaultSide, thirdDefaultSide):
        solutions += perimeterConstruction(defaultSide)
        
    for newSide in getNextSideOfHeronianTriangle(firstDefaultSide, secondDefaultSide, thirdDefaultSide):
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
    createPerimeterForNNNPlusOne = lambda x: x * 3 + 1
    
    solutions += constructValidHeronianTriangles(createPerimeterForNNNPlusOne, LIMIT, *defaultNNNPlusOneSides)
    
    # now, calculate the n, n, n-1 triangles.
    defaultNNNMinusOneSides = (17, 241, 3361)
    createPerimeterForNNNMinusOne = lambda x: x * 3 - 1   
    
    solutions += constructValidHeronianTriangles(createPerimeterForNNNMinusOne, LIMIT, *defaultNNNMinusOneSides)
    
    print "Solutions:", solutions    
        

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."