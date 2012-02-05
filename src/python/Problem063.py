'''
Created on Feb 4, 2012

@author: mchrzanowski
'''

from time import time

FIRST_NUMBER = 1
LAST_NUMBER = 9

def main():
    ''' we are looking a very limited subset of numbers here. 
    10^n is too large for any n. So for any base number < 10,
    we stop checking powers once the power > number of digits '''
    
    start = time()
    solutionSet = set([])
    for i in xrange(FIRST_NUMBER, LAST_NUMBER + 1):
        power = 0
        candidate = 1
        while power <= len(str(candidate)):
            power += 1
            candidate *= i
            
            if len(str(candidate)) == power:
                solutionSet.add(candidate)
            
         
    print "Solutions: ", len(solutionSet)
    end = time()
    print "Runtime: ", end - start, " seconds. "

if __name__ == '__main__':
    main()