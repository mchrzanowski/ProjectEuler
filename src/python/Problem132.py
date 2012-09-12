'''
Created on Sep 10, 2012

@author: mchrzanowski
'''

from math import log
from ProjectEulerLibrary import generate_next_prime


def main(repunit_length, number_of_primes_to_find):

    prime_factors = set()

    primes = generate_next_prime()

    # avg. number of distinct primes is ~ lg lg n
    # or about ln(2.3 * log10(10 ** repunit_length))
    if number_of_primes_to_find > 2 * log(2.3 * repunit_length):
        raise Exception("This number can't have so many unique factors!")

    while len(prime_factors) != number_of_primes_to_find:

        new_prime = primes.next()

        # a base-10 repunit is formed via the following forumula:
        # (10 ** (number of digits) - 1) / (10 - 1)

        # we use modular exponentiation to see whether
        # 10 ** (number of digits) is divisible by 9 * some prime
        # with remainder 1.

        if pow(10, repunit_length, 9 * new_prime) == 1:
            prime_factors.add(new_prime)

    print "Sum of first %d factors: %d" % (number_of_primes_to_find,
        sum(prime_factors))


if __name__ == '__main__':
    import argparse
    import time

    start = time.time()

    parser = argparse.ArgumentParser(
        description="Problem 132. URL: http://projecteuler.net/problem=132")
    parser.add_argument('-R', type=int, help="Number of digits in the base-10 repunit.")
    parser.add_argument('-n', type=int, help="Number of unique primes to find.")
    args = vars(parser.parse_args())

    main(args['R'], args['n'])
    end = time.time()
    print "Runtime: %f seconds" % (end - start)
