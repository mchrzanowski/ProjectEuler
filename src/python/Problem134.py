'''
Created on Aug 31, 2012

@author: mchrzanowski
'''

from math import log10
from ProjectEulerLibrary import crt, generate_next_prime


def main(max_number):

    summation = 0
    prime_generator = generate_next_prime(start=5)

    first_prime = prime_generator.next()

    while first_prime <= max_number:

        second_prime = prime_generator.next()

        # we have the two following congruence relations:
        # x = 0 (mod second_prime)
        # x = first_prime(mod 10 ** (int(log10(first_prime)) + 1))
        # so we use the Chinese Remainder Theorem to solve for x.

        # thanks to Eigenray from http://projecteuler.net/thread=134
        # for the suggestion to use CRT.

        modulos = (second_prime, (10 ** (int(log10(first_prime)) + 1)),)
        remainders = (0, first_prime,)

        summation += crt(modulos, remainders)

        #print first_prime, second_prime, residual
        first_prime = second_prime

    print "Sum(S) : %d" % summation


if __name__ == '__main__':
    import argparse
    import time

    begin = time.time()

    parser = argparse.ArgumentParser(
        description="Problem 134. URL: http://projecteuler.net/problem=134")
    parser.add_argument('-n', type=int, help="Max ceiling to look for primes.")
    args = vars(parser.parse_args())
    main(args['n'])

    end = time.time()
    print "Runtime: %f seconds." % (end - begin)
