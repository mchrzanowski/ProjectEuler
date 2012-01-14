'''
Created on Jan 9, 2012

@author: mchrzanowski
'''
from time import time


LIMIT = 1001

def main():
    start = time()
    oddOffsets = {}
    offset = 0
    for i in range(1, LIMIT + 1):
        if i % 2 is not 0:
            oddOffsets[i ** 2] = offset
 #           print i ** 2 , " : ", offset
            offset = offset + 1
    listOfOddNumbers = extractSpiralDiagonals(oddOffsets)
    print "Sum of Diagonals: ", sum(listOfOddNumbers)
    end = time()
    print "Time: ", end - start, " s."

def extractSpiralDiagonals(offsetDict):
    oddList = []
    currentOffsetUsed = 0
    tempOffsetCounter = 0
    for i in range(1, LIMIT ** 2 + 1):
        if i in offsetDict:
            currentOffsetUsed = tempOffsetCounter = offsetDict[i]
            oddList.append(i)
        elif i % 2 is not 0:
            tempOffsetCounter = tempOffsetCounter - 1
            if tempOffsetCounter == -1:
                oddList.append(i)
                tempOffsetCounter = currentOffsetUsed
    return oddList
        
    
if __name__ == '__main__':
    main()  