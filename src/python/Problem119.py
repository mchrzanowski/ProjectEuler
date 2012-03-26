'''
Created on Mar 26, 2012

@author: mchrzanowski
'''

from time import time

def main():
    
    baseNumber = 2
    LIMIT = 30
    POW_LIMIT = 30
    
    sumDigitsInNumber = lambda number: sum([int(digit) for digit in str(number)])
    
    solutions = set()
    
    while len(solutions) < 2 * LIMIT:   # we go over what we need as there might be results created from
                                        # smaller powers of larger numbers. we'll need to sort...
        power = 2
        while power < POW_LIMIT:        # without a theoretical ceiling that limits the max power, we 
                                        # just assume that this is a sufficiently high ceiling to use.
            result = baseNumber ** power            
            if sumDigitsInNumber(result) == baseNumber:
                solutions.add(result)
#                print baseNumber, power, result
            
            power += 1
        
        baseNumber += 1
            
    print "A_%d: %d" % (LIMIT, sorted(list(solutions))[LIMIT - 1])
        
if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."