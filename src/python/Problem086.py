'''
Created on Apr 30, 2012

@author: mchrzanowski

USE PYPY ONLY
'''

from math import sqrt
from time import time

    
def main(): 
    
    M = 1818
    solutions = 0
    
    for i in xrange(1, M + 1):
        for j in xrange(i, M + 1):
            for k in xrange(j, M + 1):
                
                # three strategies
                
                one = i ** 2 + (j + k) ** 2
                two = j ** 2 + (i + k) ** 2
                three = k ** 2 + (i + j) ** 2
                
                if one < two:
                    minimum = one
                else:
                    minimum = two
                    
                if minimum > three:
                    minimum = three
                                
                if sqrt(minimum).is_integer():
                    solutions += 1
                    
    print M, ":", solutions
                

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."