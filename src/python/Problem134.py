'''
Created on Aug 31, 2012

@author: mchrzanowski
'''

from math import log10
from ProjectEulerPrime import ProjectEulerPrime


def generate_next_prime(start=2):

    # since 2 is the only even number,
    # immediately yield it and start
    # the below loop at the first odd prime.
    if start == 2:
        yield 2
        start = 3

    prime_object = ProjectEulerPrime()
    while True:
        if prime_object.isPrime(start):
            yield start
        start += 2


def main(max_number):

    summation = 0
    prime_generator = generate_next_prime(start=5)

    first_prime = prime_generator.next()

    while True:

        second_prime = prime_generator.next()

        if first_prime > max_number:
            break

        # we have the congruence relation:
        # first_prime = second_prime (mod 10 ** (int(log10(first_prime)) + 1))
        # so, we simply have to add 10 ** (int(log10(first_prime)) + 1)
        # to first prime until we get a number that is a multiple of
        # second_prime
        increment = 10 ** (int(log10(first_prime)) + 1)
        first_section = increment
        while True:
            residual = first_section + first_prime
            if residual % second_prime == 0:
                break
            first_section += increment

        #print first_prime, second_prime, residual
        summation += residual
        first_prime = second_prime

    print summation


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
