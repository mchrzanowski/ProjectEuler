'''
Created on Jan 13, 2012

@author: mchrzanowski
'''

from time import time

LIMIT = 200

def dynamicIteration(): 
    i = 0
    for a in xrange(0, LIMIT + 1, 200):
        for b in xrange(0, LIMIT + 1 - a, 100):
            for c in xrange(0, LIMIT + 1 - a - b, 50):
                for d in xrange(0, LIMIT + 1 - a - b - c, 20):
                    for e in xrange(0, LIMIT + 1 - a - b - c - d, 10):
                        for f in xrange(0, LIMIT + 1 - a - b - c - d - e, 5):
                            for g in xrange(0, LIMIT + 1 - a - b - c - d - e - f, 2):
                                for h in xrange(0, LIMIT + 1 - a - b - c - d - e - f - g, 1):
                                    if a + b + c + d + e + f + g + h == LIMIT:
                                        i += 1
    return i
 
def main(): 
    begin = time()
    print dynamicIteration()
    end = time()
    print "Runtime: ", end - begin, " seconds. "

if __name__ == '__main__':
    main()
