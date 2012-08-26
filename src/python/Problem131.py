'''
Created on Aug 25, 2012

@author: mchrzanowski
'''

from ProjectEulerPrime import ProjectEulerPrime


def main(ceiling):

    primes = ProjectEulerPrime()
    special_primes = 0

    # n ** 3 + p * n ** 2 = x ** 3 can be re-written as:
    # n ** 2 * (n + p) = x ** 3
    # since x, p, and n are positive integers, we know that
    # n ** 2 and (n + p) must be themselves perfect cubes.
    # furthermore, if you inspect the first few primes that
    # have the special property of the problem, you see this pattern:
    #   p + n = perfect cube (root)
    #   7 + 1 = 8 (2)
    #   19 + 8 = 27 (3)
    #   37 + 27 = 64 (4)
    #   61 + 64 = 125 (5)
    #   127 + 216 = 343 (7)
    # you see that the prime # is that which pushes x ** 3 -> (x + 1) ** 3
    # it's also not 100% in effect (n=125, perfect cube = 216)

    root = 1
    while True:

        difference = (root + 1) ** 3 - root ** 3
        # you can see that the gulf between two adjacent perfect cubes
        # is going to grow larger and larger. eventually, the prime falls out
        # of our scope.
        if difference >= ceiling:
            break
        elif primes.isPrime(difference):
            special_primes += 1

        root += 1

    print "Number of special primes below %d: %d" % (ceiling, special_primes)

if __name__ == '__main__':
    import argparse
    import time

    begin = time.time()

    parser = argparse.ArgumentParser(
        description="Problem 131. URL: http://projecteuler.net/problem=131")
    parser.add_argument('-max', type=int, help="Maximum numerical ceiling.")
    args = vars(parser.parse_args())
    main(args['max'])

    end = time.time()
    print "Runtime: %f seconds" % (end - begin)
