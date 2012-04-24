'''
Created on Apr 22, 2012

@author: mchrzanowski
'''

from time import time

def main():
    
    LIMIT = 50
    countingDict = {0: 1, -1: 0, -2: 0, -3: 0}
    
    for i in xrange(1, LIMIT + 1):
        countingDict[i] = countingDict[i - 1] + countingDict[i - 2] + countingDict[i - 3] + countingDict[i - 4]
    
    print "Solution: ", countingDict[LIMIT]

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."