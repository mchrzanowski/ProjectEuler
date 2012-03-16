'''
Created on Mar 15, 2012

@author: mchrzanowski
'''
from time import time

def main():
    
    LIMIT = 0.99
    
    iteration = 101         # 101 is the first bouncy number
    bouncies = 0
    
    while float(bouncies) / iteration != LIMIT:
        
        strIteration = str(iteration)
        monoIncrease = monoDecrease = True
        
        for digitPlace in xrange(0, len(strIteration) - 1):
            if strIteration[digitPlace] < strIteration[digitPlace + 1]:
                monoDecrease = False
            elif strIteration[digitPlace] > strIteration[digitPlace + 1]:
                monoIncrease = False
            
            if not monoIncrease and not monoDecrease:
                bouncies += 1
                break
        
        iteration += 1

    print "Number for which ", (LIMIT * 100), "% of numbers are bouncies:",
    print iteration

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."