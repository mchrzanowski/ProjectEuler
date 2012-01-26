'''
Created on Jan 26, 2012

@author: mchrzanowski
'''

from time import time

FIRST_MULTIPLIER = 2
LAST_MULTIPLIER = 6

def main():
    
    start = time()
    
    solution = 0
    candidate = 10          # at the very minimum, this can't be < 10. 
        
    while solution == 0:
        
        strCandiate = str(candidate)
        
        charSet = set([char for char in strCandiate])
        
        isCandidateASolution = True
        
        for i in xrange(FIRST_MULTIPLIER, LAST_MULTIPLIER + 1):
            multipliedCandidateStr = str(i * candidate)

            if len(strCandiate) != len(multipliedCandidateStr) or \
            charSet != set([char for char in multipliedCandidateStr]):
                isCandidateASolution = False
                break
        
        if isCandidateASolution:
            solution = candidate
        else:
            candidate += 1
    
    end = time()
    print "Solution: ", solution
    print "Runtime: ", end - start, " seconds. "

if __name__ == '__main__':
    main()