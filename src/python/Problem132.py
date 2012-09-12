'''
Created on Sep 10, 2012

@author: mchrzanowski
'''

from math import log
from ProjectEulerLibrary import generate_next_prime


def main():

    # it's hard to know whether a number even
    # has a given number of prime factors
    # (avg case is ln ln n). so, disallow
    # the user from inputting a given number
    # of prime factors to find like I might normally do.

    repunit_length = 10 ** 9
    number_of_primes_to_find = 40

    prime_factors = set()
    primes = generate_next_prime()

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
    import time

    start = time.time()
    main()
    end = time.time()
    print "Runtime: %f seconds" % (end - start)
