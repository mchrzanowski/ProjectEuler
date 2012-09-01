'''
Created on Aug 28, 2012

@author: mchrzanowski
'''

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

        # must remain odd as first_prime is odd
        # and odd * even -> even.
        coefficient = 3

        str_first_prime = str(first_prime)

        while not str(coefficient * second_prime).endswith(str_first_prime):
            coefficient += 2

        #print first_prime, second_prime, coefficient, coefficient * second_prime
        summation += coefficient * second_prime
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
