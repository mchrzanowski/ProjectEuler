'''
Created on May 16, 2012

@author: mchrzanowski
'''

from itertools import combinations
from time import time


# functions that check whether each square number can be created from the input collections.
# allow 6 and 9 to be interchangeable
create_1 = lambda x, y: (0 in x and 1 in y) or (0 in y and 1 in x)
create_4 = lambda x, y: (0 in x and 4 in y) or (0 in y and 4 in x)
create_9 = lambda x, y: (0 in x and (6 in y or 9 in y)) or (0 in y and (6 in x or 9 in x))
create_16 = lambda x, y: (1 in x and (6 in y or 9 in y)) or (1 in y and (6 in x or 9 in x))
create_25 = lambda x, y: (2 in x and 5 in y) or (2 in y and 5 in x)
create_36 = lambda x, y: (3 in x and (6 in y or 9 in y)) or (3 in y and (6 in x or 9 in x))
create_49 = lambda x, y: (4 in x and (6 in y or 9 in y)) or (4 in y and (6 in x or 9 in x))
create_64 = lambda x, y: ((6 in x or 9 in x) and 4 in y) or ((6 in y or 9 in y) and 4 in x)
create_81 = lambda x, y: (8 in x and 1 in y) or (8 in y and 1 in x)
        
def main():
        
    solutions = 0
    digit_pool = frozenset(number for number in xrange(0, 9 + 1))
    
    for x in combinations(digit_pool, 6):
        for y in combinations(digit_pool, 6):
            
            if create_1(x, y) and create_4(x, y) and create_9(x, y) and create_16(x, y) and create_25(x, y) \
            and create_36(x, y) and create_49(x, y) and create_64(x, y) and create_81(x, y):
                solutions += 1
    
    solutions /= 2  # we're going to double-count the solutions
                
    print "Distinct arrangements:", solutions
            
if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."
