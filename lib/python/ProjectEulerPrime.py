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
        n = int(n)
        if n < 2:
            return False
        elif n == 2:
            return True
        elif n & 1 == 0:
            return False
        elif not Prime.factor(self, n):
            return True
        else:
            return False
