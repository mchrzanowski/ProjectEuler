'''
Created on Jan 13, 2012

@author: mchrzanowski
'''

from time import time
import numpy as np

LIMIT = 200
COINS = (1, 2, 5, 10, 20, 50, 100, 200)

# O(LIMIT * |COINS|)
def dp():
    M = np.zeros((LIMIT + 1, len(COINS) + 1), dtype=np.int)

    # base cases.
    for i in xrange(1, LIMIT + 1):
        M[i, 1] = 1  # there's 1 way to produce n with only the first coin.

    for c in xrange(1, len(COINS) + 1):
        M[1, c] = 1  # there's 1 way to produce $1.
        M[0, c] = 1  # number matches the coin.

    for c in xrange(2, len(COINS) + 1):
        for n in xrange(2, LIMIT + 1):
            M[n, c] = M[n, c - 1]
            if n - COINS[c - 1] >= 0:
                M[n, c] += M[n - COINS[c - 1], c]

    return M[LIMIT, len(COINS)]

# O(LIMIT ^ |COINS|)
def bruteForce():
    i = 0
    for a in xrange(0, LIMIT + 1, COINS[-1]):
        for b in xrange(0, LIMIT + 1 - a, COINS[-2]):
            for c in xrange(0, LIMIT + 1 - a - b, COINS[-3]):
                for d in xrange(0, LIMIT + 1 - a - b - c, COINS[-4]):
                    for e in xrange(0, LIMIT + 1 - a - b - c - d, COINS[-5]):
                        for f in xrange(0, LIMIT + 1 - a - b - c - d - e, COINS[-6]):
                            for g in xrange(0, LIMIT + 1 - a - b - c - d - e - f, COINS[-7]):
                                for h in xrange(0, LIMIT + 1 - a - b - c - d - e - f - g, COINS[-8]):
                                    if a + b + c + d + e + f + g + h is LIMIT:
                                        i += 1

    return i

def _run(func, name):
    begin = time()
    print "Answer: %s" % func()
    end = time()
    print "%s Runtime: %s secs." % (name, end - begin)

def main():
    _run(dp, "DP")
    _run(bruteForce, "Bruce Force")

if __name__ == '__main__':
    main()
