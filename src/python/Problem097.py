'''
Created on Jan 22, 2012

@author: mchrzanowski
'''

from time import time

LIMIT = 10

def main():
    
    start = time()
    print "Last ten digits: ", (28433 * 2 ** 7830457 + 1) % 10 ** LIMIT
    end = time()
    print "Runtime: ", end - start, " seconds. "

if __name__ == '__main__':
    main()