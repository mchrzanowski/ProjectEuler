'''
Created on Mar 26, 2012

@author: mchrzanowski
'''

from time import time

def main():
    
    iteration = 2
    LIMIT = 30
    POW_LIMIT = 30
    
    sumDigitsInNumber = lambda x: sum([int(number) for number in str(x)])
    
    solutions = set()
    
    while len(solutions) < 2 * LIMIT:   # we go over what we need as there might be results created from
                                        # smaller powers of larger numbers. we'll need to sort...
        power = 2
        while power < POW_LIMIT:        # without a theoretical ceiling that limits the max power, we 
                                        # just assume that this is a sufficiently high ceiling to use.
            result = iteration ** power            
            if sumDigitsInNumber(result) == iteration:
                solutions.add(result)
#                print iteration, power, value
            
            power += 1
        
        iteration += 1
            
    print "A_%d: %d" % (LIMIT, sorted(list(solutions))[LIMIT - 1])
        
if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."