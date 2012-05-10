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

def main():
    
    # recurrence relationships received from:
    # http://www.had2know.com/academics/nearly-equilateral-heronian-triangles.html
    
    LIMIT = 1 * 10 ** 9
    solutions = 0

    # first, calculate the n, n, n+1 heronian isosceles triangles.
    # seed the recurrence relation method with the first 3 n I found by hand that 
    # create valid triangles   
    defaultNNNPlusOneSides = (5, 65, 901)     
    nNNPlusOne = recurrenceRelation(defaultNNNPlusOneSides[0], defaultNNNPlusOneSides[1], defaultNNNPlusOneSides[2])
    createPerimeterFromPlusOne = lambda x: x * 3 + 1
    
    for defaultSide in defaultNNNPlusOneSides:
        solutions += createPerimeterFromPlusOne(defaultSide)
        
    for newSide in nNNPlusOne:
        if createPerimeterFromPlusOne(newSide) <= LIMIT:
            solutions += createPerimeterFromPlusOne(newSide)
        else:
            break
    
    # now, calculate the n, n, n-1 triangles.
    defaultNNNMinusOneSides = (17, 241, 3361)
    nNNMinusOne = recurrenceRelation(defaultNNNMinusOneSides[0], defaultNNNMinusOneSides[1], defaultNNNMinusOneSides[2])
    createPerimeterFromMinusOne = lambda x: x * 3 - 1
    
    for defaultSide in defaultNNNMinusOneSides:
        solutions += createPerimeterFromMinusOne(defaultSide)
    
    for newSide in nNNMinusOne:
        if createPerimeterFromMinusOne(newSide) <= LIMIT:
            solutions += createPerimeterFromMinusOne(newSide)
        else:
            break


    print "Solutions:", solutions    
        

if __name__ == '__main__':
    start = time()
    main()
    end= time()
    print "Runtime:", end - start, "seconds."