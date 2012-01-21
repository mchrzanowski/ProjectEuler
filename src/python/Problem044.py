'''
Created on Jan 21, 2012

@author: mchrzanowski
'''
from time import time

LIMIT = 10000    # since the pentagonal generator increases by n^2 for each n, we want the smallest pair of pentagonals possible
                # whose sums and differences are both pentagonal. So the limit can't be too great; set the limit to be 10,000.

def generatePentagonalNumbers(numberLimit):
    for i in xrange(1, numberLimit + 1):
        yield i * (3 * i - 1) / 2
        

def main():
    
    start = time()
    
    solutionList = []
    
    pentagonalList = [number for number in generatePentagonalNumbers(LIMIT)]
    pentagonalSet = set(pentagonalList)     # for speed
    
    i = 0
    while len(solutionList) == 0:
        for j in xrange(i, len(pentagonalList)):
            if pentagonalList[i] + pentagonalList[j] in pentagonalSet and \
            abs(pentagonalList[i] - pentagonalList[j]) in pentagonalSet:
                solutionList.append(pentagonalList[i])
                solutionList.append(pentagonalList[j])
        i += 1
    
    
    print "Solutions: ", solutionList
    print "|Difference|: ", abs(solutionList[1] - solutionList[0])
            
    end = time()
    
    print "Runtime: ", end - start, " seconds."
    

if __name__ == '__main__':
    main()