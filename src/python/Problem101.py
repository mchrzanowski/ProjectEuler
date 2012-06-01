'''
Created on May 31, 2012

@author: mchrzanowski
'''

from __future__ import division
from time import time

class Point(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        return other.x == self.x and other.y == self.y
    
    def __ne__(self, other):
        return other.x != self.x or other.y != self.y
    
    def __str__(self):
        return "x:%f\ty:%f" % (self.x, self.y) 


def fit_polynomial_function_and_get_next_point(points, new_x):
    ''' 
        use the LaGrange polynomial function generator algorithm given at:
        # http://en.wikipedia.org/wiki/Lagrange_polynomial
        to fit a function and then get the next point 
    '''
    
    new_y = 0
    
    for point in points:
                
        temporary_y = 1
        
        for other_point in points:
            
            if other_point == point:
                continue
            
            temporary_y *= (new_x - other_point.x) / (point.x - other_point.x)
            
        new_y += point.y * temporary_y
            
    return Point(new_x, int(round(new_y)))      # assume the nearest integer


def true_sequence_generator():
    ''' this method generates a sequence of numbers from the correct polynomial function '''
    number = 1
    while True:
        result = 0
        for power in xrange(0, 10 + 1):
            result += (-1) ** power * number ** power
        yield result
        number += 1

def main(): 
    
    
    bad_terms = 0
    
    sequence_generator = enumerate(true_sequence_generator())
    
    first_point = sequence_generator.next()
    
    list_of_true_points = [Point(first_point[0] + 1, first_point[1])]
        
    for x, y in sequence_generator:
                
        next_theoretical_point = fit_polynomial_function_and_get_next_point(list_of_true_points, x + 1)
                
        list_of_true_points.append(Point(x + 1, y))
                        
        if next_theoretical_point == list_of_true_points[-1]:
            break
        
        bad_terms += next_theoretical_point.y
    
    
    print "Sum of bad terms encountered before the correct polynomial fitting was discovered:", bad_terms

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."

