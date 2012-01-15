'''
Created on Jan 15, 2012

@author: mchrzanowski
'''

from time import time

LIMIT = 1963    # found through numerical analysis
PANDIGITAL_NUMBERS = 9

def stringIsPandigital(numberString):
    
    if len(numberString) is not PANDIGITAL_NUMBERS:
        return False
    
    if '0' in numberString:
        return False
        
    if len(set([char for char in numberString])) is PANDIGITAL_NUMBERS:
        return True
    
    return False

def main():
    
    start = time()

    possibilities = set([])
    
    for i in xrange(1, LIMIT + 1):
        for j in xrange(i + 1, LIMIT + 1):
            product = i * j
            if stringIsPandigital(str(i) + str(j) + str(product)):
                possibilities.add(product)
                
    print "Sum of all Unique Products: ", sum(possibilities)
    
    end = time()
    
    print "Runtime: ", end - start, " seconds."

if __name__ == '__main__':
    main()