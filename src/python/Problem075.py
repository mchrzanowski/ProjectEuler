'''
Created on Mar 2, 2012

@author: mchrzanowski
'''

from fractions import gcd
from time import time

LIMIT = 15 * 10 ** 5

def main():
    
    '''
    the problem is asking to find the unique sums of pythagorean triplets
    use the algo given by:
    http://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
    
    we store two sets: one for all unique sums, and one for storing sums that are non-unique.
    since Euclid's formula uncovers all pythagorean triplets, we can simply check to see
    whether a given sum is already present in uniqueSums. if it is, then remove it from the set
    and add it to the non-unique set.
    '''
    
    uniqueSums = set([])
    duplicateSums = set([])
    
    
    for m in xrange(2, int(LIMIT ** 0.5) + 1):  # since c = m ** 2 + n ** 2, a loose upper bound is (a + b + c) ** 0.5
        
        for n in xrange(1, m):
            
            # is m - n odd?
            if m - n & 1 == 0: continue
            
            # are m and n relatively prime?
            if gcd(m, n) != 1: continue
            
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2
                    
            k = 1
            while True:
                
                newSum = k * (a + b + c)
                
                if newSum <= LIMIT:
                    if newSum in uniqueSums:       # duplicate! 
                        uniqueSums.remove(newSum)
                        duplicateSums.add(newSum)
                    elif newSum not in duplicateSums:
                        uniqueSums.add(newSum)
                else: 
                    break
                
                k += 1
    
    print "Solutions:", len(uniqueSums)

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."
