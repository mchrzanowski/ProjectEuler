'''
Created on Mar 18, 2012

@author: mchrzanowski
'''

from math import floor, sqrt
from ProjectEulerLibrary import isNumberPalindromic
from time import time

def main():
    
    rollingTotal = 1        # 1 ** 2 is special as it's palindromic, but it's only 1 number. 
                            # so start the total at 1 to avoid special casiing in the algo.
    palindromes = set([])
    LIMIT = 10 ** 8
    END = int(floor((sqrt(4 - 4 * 2 * (1 - LIMIT)) + 2) / 4))   # solve x ** 2 + (x - 1) ** 2 = LIMIT
                                                                # this establishes the very last squared number
                                                                # that, when added to the 2nd-to-last squared number,
                                                                # produces a number < LIMIT.
    for i in xrange(2, END + 1):
        
        rollingTotal += i ** 2
        
        if rollingTotal < LIMIT and isNumberPalindromic(rollingTotal): 
            palindromes.add(rollingTotal)
        
        copyOfTotal = rollingTotal
        
        for j in xrange(1, i - 1):                              # the sum is of at least two values.
            copyOfTotal -= j ** 2
            if copyOfTotal < LIMIT and isNumberPalindromic(copyOfTotal): 
                palindromes.add(copyOfTotal)
                
    print "Sum of all palindromes:", sum(palindromes)
    
if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."