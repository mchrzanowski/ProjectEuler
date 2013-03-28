from ProjectEulerLibrary import phi
from fractions import gcd


def main():

    RATIO = (15499, 94744)
    cache = dict()

    default = float('inf')
    bestSoFar = default

    '''
    So, here are the facts:
        * phi(n) gives the number of positive integers < n that are relatively prime to n.
        * if m and n are relatively prime to each other, phi(m * n) = phi(m) * phi(n).
        * phi(n) is always nearly n. 
    So we want to focus on doing as much work as possible with small n. So, the algo is as follows:
        1). iterate from 2 to infinity. Call this i.
        2). calculate phi(i). store this in a cache.
        3). find phi(m * i) for each m in the cache.
        4). if we find an element that works, stop the iteration (since the keys are unordered, go through
            all keys first and pick the smallest m * i).
    '''

    i = 2
    while True:
        value = phi(i)
        cache[i] = value
        for num in cache.keys():
            if gcd(num, i) == 1:
                cache[num * i] = cache[num] * value
                if num * i < bestSoFar and (RATIO[1] * cache[num * i]) < ((num * i - 1) * RATIO[0]):
                    bestSoFar = num * i
        if bestSoFar != default:
            break
        else:
            i += 1

    print "Solution: {}".format(bestSoFar)

if __name__ == '__main__':
    import argparse
    import time

    start = time.time()

    parser = argparse.ArgumentParser(description="Problem 234. URL: http://projecteuler.net/problem=234")
    main()

    end = time.time()
    print "Runtime: {} seconds.".format(end - start)
