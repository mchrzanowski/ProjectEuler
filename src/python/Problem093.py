'''
Created on May 15, 2012

@author: mchrzanowski
'''

from itertools import combinations, permutations
from operator import add, mul, sub, truediv
from time import time


def create_target_numbers(a, b, c, d):
    # there are 5 combinations of parentheses that could work here.
    # there are 4 ** 3 possible arithmetic operations to use on the 4 variables.
    # thus creating 5 * 4 ** 3 = 302 potential target numbers per function call.
    target_numbers = set()
    operators = frozenset((add, truediv, mul, sub))

    for op_1 in operators:
        for op_2 in operators:
            for op_3 in operators:
                
                # because we are applying the operations naively,
                # there's a real possibility of division by zero. ergo, wrap each sequence
                # of operations in a try/catch block.
                
                try:
                    solution_1 = op_3(op_2(op_1(a, b), c), d)      # (((a b) c) d)
                except ZeroDivisionError:
                    solution_1 = -1
                
                try:
                    solution_2 = op_3(op_1(a, b), op_2(c, d))      # ((a b) (c d))
                except ZeroDivisionError:
                    solution_2 = -1
                
                try:    
                    solution_3 = op_3(op_2(a, op_1(b, c)), d)    # ((a (b c)) d)
                except ZeroDivisionError:
                    solution_3 = -1
                
                try:    
                    solution_4 = op_3(a, op_2(op_1(b, c), d))     # (a ((b c) d))
                except ZeroDivisionError:
                    solution_4 = -1
                
                try:
                    solution_5 = op_3(a, op_2(b, op_1(c, d)))     # (a (b (c d)))
                except ZeroDivisionError:
                    solution_5 = -1
                
                for solution in (solution_1, solution_2, solution_3, solution_4, solution_5):
                    if solution == int(solution) and solution > 0:
                        target_numbers.add(int(solution))
                
    return target_numbers

def main():
    
    digit_pool = frozenset(number for number in xrange(1, 9 + 1))
    max_run = 0
    max_key = None
    
    for combination in combinations(digit_pool, 4):
                            
        target_numbers = set()
        
        for permutation in permutations(combination, 4):
            target_numbers.update(create_target_numbers(*permutation))
        

        # iterate through our set and get the length of the consecutive run.
        run_length = 0
        previous_value = None
        
        for value in sorted(target_numbers):
            if previous_value is None or value == previous_value + 1:
                run_length += 1
                previous_value = value
            else:
                break
        
        if run_length > max_run:
            max_run = run_length
            max_key = ''.join(str(digit) for digit in combination)
            
    
    print "abcd:", max_key
    print "Greatest run of consecutive numbers:", max_run
                    

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime", end - start, "seconds."
