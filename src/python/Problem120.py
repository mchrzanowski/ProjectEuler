'''
Created on Mar 20, 2012

@author: mchrzanowski
'''

from ProjectEulerPrime import ProjectEulerPrime
from time import time

def main():
    ''' 
    this was solved purely through empirical analysis.
    the largest mod value for primes was found through the formula:
        incrementor * i + i
    where incrementor is just a counter that starts at 1 for 3.
    for even numbers, it turned out to be:
        incrementor * i
    and odd composites, strangely:
        i * (i - 1)
    '''
    LIMIT = 10 ** 3
    
    p = ProjectEulerPrime()
    
    solutions = 0
    
    incrementor = 1
    
    for i in xrange(3, LIMIT + 1):
        
        if p.isPrime(i):
            solutions += incrementor * i + i
            
        elif i & 1 == 0:
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
