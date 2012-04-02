'''
Created on Mar 31, 2012

@author: mchrzanowski
'''

from time import time

def numberHasOnlyOddDigits(n):
    n = str(n)
    
    if '0' in n or  \
    '2' in n or     \
    '4' in n or     \
    '6' in n or     \
    '8' in n:
        return False
    
    return True

def main():
        
    reversibleNumbers = set()
        
    for i in xrange(1, 10 ** 8, 2):     # one of the two numbers must be odd. so skip even n.
                
        if i % 10 == 0: continue
        
        reversedNumber = int(str(i)[::-1])
                
        if numberHasOnlyOddDigits(i + reversedNumber):
            reversibleNumbers.add(i)
            reversibleNumbers.add(reversedNumber)
    
    print "Solutions: ", len(reversibleNumbers)

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print 'Runtime:', end - start, 'seconds.'
