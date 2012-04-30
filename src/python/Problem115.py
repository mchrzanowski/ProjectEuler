'''
Created on Apr 28, 2012

@author: mchrzanowski
'''

from time import time

def main():
    
    LIMIT = 1 * 10 ** 6
    M = 50
    
    countingDict = dict()
    iterator = 0
    
    while iterator < M: 
        countingDict[iterator] = 1
        iterator += 1
        
    while countingDict[iterator - 1] < LIMIT:
        countingDict[iterator] = countingDict[iterator - 1] + 1
        for j in xrange(M, iterator):
            countingDict[iterator] += countingDict[iterator - (j + 1)]
        iterator += 1
    
    print "First row that sums to > %d : %d" % (LIMIT, iterator - 1)

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."