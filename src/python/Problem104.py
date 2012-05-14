'''
Created on Mar 16, 2012

@author: mchrzanowski
'''

from math import log10
from time import time

class FibGenerator(object):
    ''' super-quick memoized fib calculator exploiting the fact that we need to calculate each fib number, 
    yet we don't need to store all previous numbers.'''

    def __init__(self):
        ''' start the variables out with the first two Fib numbers. Label the second to be the first Fib number'''
        self.previous = 0
        self.current = 1
        self.iterator = 1
        
        
    def generateNext(self):
        ''' return the next fib number as well as an identifier of which fib number this is '''
        self.previous, self.current = self.current, self.previous + self.current
        self.iterator += 1
        return self.iterator, self.current

def main():
    
    solution = 0
    pandigitals = frozenset(i for i in xrange(1, 10))
    fibGenerator = FibGenerator()    
    
    def createSetOfDigitsInNumber(number):
        setToFill = set()
        while number != 0:
            setToFill.add(number % 10)
            number /= 10
        return setToFill
        
    while solution == 0:
                
        fibNumber, result = fibGenerator.generateNext()
    
        # formula to get the first number of digits in a number came from:
        # http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html#fibinits
        # do the head check first as it's FAR faster than if the tail is checked first.
        headSet = createSetOfDigitsInNumber(int(10 ** (log10(result) - int(log10(result))) * 10 ** 8))
        
        if headSet == pandigitals:
        
            tailSet = createSetOfDigitsInNumber(result % 10 ** 9)
        
            if pandigitals == tailSet:
                solution = fibNumber
                    
    print "Solution: ", solution
        

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."