'''
Created on Mar 16, 2012

@author: mchrzanowski
'''

from math import log10
from time import time

def fib(n, cache=[0, 1]):
    ''' super-quick memoized fib calculator exploiting the fact that we need to calculate each fib number'''
    if n < 2: 
        return n
    else:
        cache[0], cache[1] = cache[1], sum(cache)
        return cache[1]
    
def main():
    
    solution = 0
    iteration = 1
    
    pandigitals = frozenset([i for i in xrange(1, 10)])
    
    def createSetOfDigitsInNumber(number):
        setToFill = set([])
        while number != 0:
            setToFill.add(number % 10)
            number /= 10
        return setToFill
        
    while solution == 0:
                
        result = fib(iteration)
    
        # formula to get the first number of digits in a number came from:
        # http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html#fibinits
        # do the head check first as it's FAR faster than if the tail is checked first.
        headSet = createSetOfDigitsInNumber(int(10 ** (log10(result) - int(log10(result))) * 10 ** 8))
        
        if headSet == pandigitals:
        
            tailSet = createSetOfDigitsInNumber(result % 10 ** 9)
        
            if pandigitals == tailSet:
                solution = iteration
        
        iteration += 1
                    
    print "Solution: ", solution
        

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."