'''
Created on Mar 31, 2012

@author: mchrzanowski
'''

from time import time

def main():
    # found through trial and error.
    # red_n = red_n-1 + red_n-2 + 1
    # green_n = green_n-1 + green_n-3 + 1
    # blue_n = blue_n-1 + blue_n-4 + 1
    
    LIMIT = 50
    
    # base cases.
    redDict = {0:0, 1:0}
    greenDict = {0:0, 1:0, 2:0}
    blueDict = {0:0, 1:0, 2:0, 3:0}
    
    for i in xrange(2, LIMIT + 1):
        redDict[i] = redDict[i - 1] + redDict[i - 2] + 1
        if i not in greenDict:
            greenDict[i] = greenDict[i - 1] + greenDict[i - 3] + 1
        if i not in blueDict:
            blueDict[i] = blueDict[i - 1] + blueDict[i - 4] + 1
    
    print "Solution: ", redDict[LIMIT] + greenDict[LIMIT] + blueDict[LIMIT]

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print 'Runtime:', end - start, 'seconds.'