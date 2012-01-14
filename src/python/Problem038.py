'''
Created on Jan 13, 2012

@author: mchrzanowski
'''

import sys
from time import time


perimeter = {}

LIMIT = 1000

def main():

    start = time()    
    for i in xrange(1, LIMIT / 3):
        for j in xrange(i + 1, LIMIT / 2):
            c = (i ** 2 + j ** 2) ** 0.5
            p = int(i + j + c)
            if p > LIMIT:
                break
            if c - int(c) <= sys.float_info.epsilon:
                if p not in perimeter:
                    perimeter[p] = 0
                perimeter[p] = perimeter[p] + 1
            
    maxSize = -1
    maxP    = -1
    for key in perimeter:
        if perimeter[key] > maxSize:
            maxSize = perimeter[key]
            maxP = key
    
    end = time()
                    
    print "maxSize: ", maxSize
    print "maxP: ", maxP
    print "Runtime: ", end - start, " secs."
                    
        
if __name__ == '__main__':
    main()