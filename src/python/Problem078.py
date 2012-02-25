'''
Created on Feb 24, 2012

@author: mchrzanowski
'''

from time import time

SUM_LIMIT = 10 ** 6
LIMIT = 6 * 10 ** 4     # found through trial and error

def main():
    numberOfWays = [0 for i in xrange(LIMIT + 1)]
    
    numberOfWays[0] = 1     # start it off
    
    solution = 0
    
    for i in xrange(1, LIMIT + 1):
                
        for j in xrange(i, LIMIT + 1): 
            numberOfWays[j]  = divmod(numberOfWays[j] + numberOfWays[j - i], SUM_LIMIT) [1]
                    
        if numberOfWays[i] == 0:
            solution = i
            break
    
    print 'Solution:', solution

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."