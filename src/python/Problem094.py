'''
Created on May 7, 2012

@author: mchrzanowski
'''

from math import sqrt
from time import time

def main():
    
    LIMIT = 1 * 10 ** 9
    solutions = 0
    
    for i in xrange(3, 1 + LIMIT / 3, 2):   # identical lengths must be odd.
        
        for j in (i - 1, i + 1):
                        
            if i + i + j > LIMIT: 
                continue
            
            # Heron's formula.
            s = float(i + i + j) / 2                         
            area = sqrt(s * (s - i) * (s - i) * (s - j))
            
            if area.is_integer():
#                print i, i, j, s, area
                solutions += i + i + j
    
    print "Solutions:", solutions
        

if __name__ == '__main__':
    start = time()
    main()
    end= time()
    print "Runtime:", end - start, "seconds."