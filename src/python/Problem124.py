'''
Created on Mar 17, 2012

@author: mchrzanowski
'''

from ProjectEulerPrime import ProjectEulerPrime
from operator import mul
from time import time


def getSortedValue(iteration, radDict):
    ''' 
    just iterate through the dict using sorted keys. we assume the list tied to a dict key
    is already sorted 
    '''
    for key in sorted(radDict.iterkeys()):
        for number in radDict[key]:
            iteration -= 1
            if iteration == 0:
                return number
    

def main():
    
    LIMIT = 10 ** 5
    ITERATION = 10 ** 4
    p = ProjectEulerPrime()
    radDict = {}                        # product(rad(n)) = list of all n with that prime factorization
    for i in xrange(1, LIMIT + 1):
        product = reduce(mul, set(p.factorize(i)))
        if product not in radDict:
            radDict[product] = [i]      # since we iterate from 1..LIMIT, use a list to store n in order.
        else:
            radDict[product].append(i)
    
    print "Solution: ", getSortedValue(ITERATION, radDict)


if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."