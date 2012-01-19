'''
Created on Jan 19, 2012

@author: mchrzanowski
'''

from time import time
LIMIT = 1000

def main():
    
    begin = time()
    series = 0
    for i in xrange(1, LIMIT + 1):
        series += i ** i
    
    print "Last ten digits: " , str(series)[-10:]
    
    end = time()
    
    print "Runtime: ", end - begin, " seconds."

if __name__ == '__main__':
    main()