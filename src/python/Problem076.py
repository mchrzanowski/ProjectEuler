'''
Created on Jan 15, 2012

@author: mchrzanowski
'''

from time import time

LIMIT = 100

def main():
    start = time()
    
    possibleNumbers = [i for i in xrange(LIMIT + 1)]
    numberOfWays = [0 for i in xrange(LIMIT + 1)]
    
    numberOfWays[0] = 1     # start it off
    
    for i in xrange(1, LIMIT + 1):
        for j in xrange(possibleNumbers[i], LIMIT + 1):
            numberOfWays[j] += numberOfWays[j - possibleNumbers[i]]

            
    for i in xrange(1, LIMIT + 1):
        numberOfWays[i] -= 1

    
    print "Combinations: ", numberOfWays[LIMIT] 
    
    end = time()
    
    print "Runtime: ", end - start, " seconds."


if __name__ == '__main__':
    main()