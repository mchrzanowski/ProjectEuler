'''
Created on Mar 20, 2012

@author: mchrzanowski
'''

from time import time

def main():
    ''' 
    this was solved purely through empirical analysis.
    the largest mod value for even numbers was found through the formula:
        incrementor * i
    where incrementor is just a counter that starts at 1 for 3.        
    and odd numbers, strangely:
        i * (i - 1)
    '''
    LIMIT = 10 ** 3
    
    
    solutions = 0
    
    incrementor = 1
    
    for i in xrange(3, LIMIT + 1):
        
        if i & 1 == 0:
            solutions += incrementor * i
            
        else:
            solutions += i * (i - 1)
            
        incrementor += 1
    
    print "Solutions:", solutions

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."
