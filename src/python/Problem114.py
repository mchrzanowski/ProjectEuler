'''
Created on Apr 28, 2012

@author: mchrzanowski
'''

from time import time

def main(): 
    
    LIMIT = 50
    countingDict = {1:1, 2:1, 3:2, 4:4, 5:7}  # base cases.
    
    for i in xrange(6, LIMIT + 1):
        countingDict[i] = countingDict[i - 1] + countingDict[i - 2] - countingDict[i - 3] + countingDict[i - 4] + countingDict[i - 5]
    
    print "Solution:", countingDict[LIMIT]

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."