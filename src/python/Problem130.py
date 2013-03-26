from math import ceil, log10
from ProjectEulerPrime import ProjectEulerPrime

def main():

    '''
    If you do the algebra, you find that:
        R(k) % n = 0
        => R(k) = a * n, where a is a natural number.
        => (10 ** k - 1) / 9 = a * n
        => 10 ** k = 9 * a * n + 1
        And so 10 ** k mod 9 * n == 1

        You also see:
        (n - 1) = b * k, where b is a natural number.
        => (n - 1) % k == 0

    '''
    current = 91    # start at first composite example.
    p = ProjectEulerPrime()
    results = set()

    while len(results) < 25:

        # obviously, 10 ** i >= (9 * current).
        for i in xrange(int(ceil(log10(9 * current))), int((current - 1) / 2.) + 1):
            if (current - 1) % i == 0 and 10 ** i % (9 * current) == 1:
                results.add(current)
                break

        while True:
            current += 2
            if current % 5 == 0: continue       # check for multiples of 5
            if p.isPrime(current): continue     # test for primality.
            break

    print "Sum: {}".format(sum(results))

if __name__ == '__main__':
    import argparse
    import time

    start = time.time()

    parser = argparse.ArgumentParser(
        description="Problem 130. URL: http://projecteuler.net/problem=130")
    main()

    end = time.time()
    print "Runtime: %f seconds." % (end - start)