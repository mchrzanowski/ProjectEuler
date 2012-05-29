'''
Created on May 22, 2012

@author: mchrzanowski

USE PYPY ONLY
'''

from itertools import combinations
from operator import mul
from ProjectEulerPrime import ProjectEulerPrime
from time import time

class FactorizationGenerator(object):
    
    def __init__(self, k, original_number, factorization):
        self.cache = set()
        self.k = k
        self.original_number = original_number
        self.factorization = factorization

    def generate_all_factorizations(self, current_factorization=None):
        ''' 
            method takes a collection of prime numbers that constitutes a given number's prime factorization.
            from there, it will multiply prime numbers together to produce composites. all potential products
            are created except for the case of all numbers being multipled together (this just produces the number 
            whose prime factorization we are looking at and is never going to be useful for us).
        '''
         
        if current_factorization is None:
            current_factorization = self.factorization
                        
        sorted_list = tuple(sorted(current_factorization))
        
        if sorted_list not in self.cache:
            
            self.cache.add(sorted_list)
            yield current_factorization
            
            for length in xrange(2, len(current_factorization)):                    # we need at least two numbers to multiply together.
                for combination in combinations(current_factorization, length):     # we also forego the creation of a single number.
                    
                        new_list = list(current_factorization)
                        for number in combination: 
                            new_list.remove(number)
                        
                        new_list.append(reduce(mul, combination))
                                            
                        for recursed_numbers in self.generate_all_factorizations(new_list):
                            yield recursed_numbers
                            
    def can_we_select_correct_factorization_using_k_numbers(self):
        
        for factorization in self.generate_all_factorizations():
            if self.original_number - sum(factorization) + len(factorization) == self.k:
                    return True
        
        return False
            
        

def main():
    
    p = ProjectEulerPrime()
    
    solutions = set()
    
    LIMIT = 12000
        
    for k in xrange(2, LIMIT + 1):
                
        for i in xrange(k, 2 * k + 1):  # found via trial and error to the the range in which this number exists for a given k.
            
            factorization_generator = FactorizationGenerator(k = k, original_number = i, factorization = p.factorize(i))
                                    
            if factorization_generator.can_we_select_correct_factorization_using_k_terms():
                solutions.add(i)
                break

    print "Solutions:", sum(solutions)


if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."
