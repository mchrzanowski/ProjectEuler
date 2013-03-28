from ProjectEulerLibrary import phi
from fractions import gcd


def main():

    RATIO = (15499, 94744)
    cache = dict()

    bestSoFar = float('inf')

    check = lambda x, y: (RATIO[1] * x) < ((y - 1) * RATIO[0])

    i = 2
    while i < bestSoFar:
        if i in cache:
            value = cache[i]
        else:
            value = phi(i)
            cache[i] = value
            for num in cache.keys():
                if gcd(num, i) == 1:
                    cache[num * i] = cache[num] * value
                    if num * i < bestSoFar and check(cache[num * i], num * i):
                        print num * i, num, i
                        bestSoFar = num * i
        
        if i < bestSoFar and check(value, i):
            print i
            bestSoFar = i
            break
        i += 1

if __name__ == '__main__':
    import argparse
    import time

    start = time.time()

    parser = argparse.ArgumentParser(description="Problem 234. URL: http://projecteuler.net/problem=234")
    main()

    end = time.time()
    print "Runtime: {} seconds.".format(end - start)
