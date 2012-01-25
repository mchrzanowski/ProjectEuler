'''
Created on Jan 24, 2012

@author: mchrzanowski
'''

from Prime import Prime

class ProjectEulerPrime(Prime):
    '''
    A subclass for the excellent prime library I found.
    '''
    
    def __init__(self):
        Prime.__init__(self)
    
    def isPrime(self, n):
        n = long(n)
        if n < 2L:
        	return False
        elif not Prime.factor(self, n):
            return True
        else:
            return False