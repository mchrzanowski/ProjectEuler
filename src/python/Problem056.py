'''
Created on Jan 28, 2012

@author: mchrzanowski
'''
from time import time

LIMIT = 100

def main():
    maxSum = 0
    
    start = time()
    for i in xrange(2, LIMIT):
        if i % 10 == 0:         # remove trivial cases. 
            continue            
        tProduct = i
        for j in xrange(2, LIMIT):
            tProduct *= i
            if j % 10 == 0:
                continue
            tSum = sum([int(char) for char in str(tProduct)])
            if  tSum > maxSum:
                maxSum = tSum
    
    print "Max sum of digits ", maxSum
    end = time()
    print "Runtime: ", end - start, " seconds."

if __name__ == '__main__':
    main()