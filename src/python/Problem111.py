'''
Created on Aug 28, 2012

@author: mchrzanowski
'''

from ProjectEulerPrime import ProjectEulerPrime


def get_primes_from_repeated_zeroes(digits, primes=ProjectEulerPrime()):
    '''
        if zero, then we know (through empirical analysis) that we have
        to change the first and last digits.
    '''
    source = list('0' * digits)
    for first_replacement_number in xrange(1, 9 + 1):

        source[0] = str(first_replacement_number)

        for second_replacement_number in xrange(1, 9 + 1):

            source[len(source) - 1] = str(second_replacement_number)
            candidate_number = int(''.join(source))

            if primes.isPrime(candidate_number):
                yield candidate_number


def get_primes_by_changing_one_digit(repeated_digit, digits,
    primes=ProjectEulerPrime()):
    '''
        using a given digit to repeat and the length of the numbers we're
        interested in, alter one place at a time with a digit and see
        whether that results in a prime number. if so, yield it.
    '''
    source = list(str(repeated_digit) * digits)
    for substitution_place in xrange(len(source)):

        candidate = list(source)

        for replacement_number in \
        (value for value in xrange(0, 9 + 1) if value != repeated_digit):

            # first number can't be 0 as that would shrink the number of
            # digits.
            if replacement_number == 0 and replacement_number == 0:
                continue

            candidate[substitution_place] = str(replacement_number)
            candidate_number = int(''.join(candidate))

            if primes.isPrime(candidate_number):
                yield candidate_number


def get_primes_by_changing_two_digits(repeated_digit, digits,
    primes=ProjectEulerPrime()):
    ''' similar to the algo above, but alter two digits instead of 1 '''

    source = list(str(repeated_digit) * digits)

    for first_sub_place in xrange(len(source)):

        for second_sub_place in (value for value in xrange(len(source)) \
        if value != first_sub_place):

            candidate = list(source)

            for first_repl_number in \
            (value for value in xrange(0, 9 + 1) if value != repeated_digit):

                # first number can't be 0 as that would shrink the number of
                # digits.
                if first_repl_number == 0 and first_sub_place == 0:
                    continue

                candidate[first_sub_place] = str(first_repl_number)

                for second_repl_number in (value for value in \
                xrange(0, 9 + 1) if value != repeated_digit):

                    if second_repl_number == 0 and second_sub_place == 0:
                        continue

                    candidate[second_sub_place] = str(second_repl_number)
                    candidate_number = int(''.join(candidate))

                    if primes.isPrime(candidate_number):
                        yield candidate_number


def main(digits):
    '''
        through trial and error, I've found that most primes can be created
        by just altering one number (at least for digits=2..13).
        the rest can be created by altering two places.
    '''

    primes = ProjectEulerPrime()
    special_primes = dict()

    for repeated_digit in xrange(0, 9 + 1):

        special_primes[repeated_digit] = set()

        # zero is a special case as we just need to alter the first and
        # last numbers.
        if repeated_digit == 0:
            for prime in get_primes_from_repeated_zeroes(digits, primes):
                special_primes[repeated_digit].add(prime)

        else:
            # swap one number.
            for prime in get_primes_by_changing_one_digit(
            repeated_digit, digits, primes):
                special_primes[repeated_digit].add(prime)

        if len(special_primes[repeated_digit]) == 0:
            # swap two numbers.
            for prime in get_primes_by_changing_two_digits(
            repeated_digit, digits, primes):
                special_primes[repeated_digit].add(prime)

        if len(special_primes[repeated_digit]) == 0:
            # trouble.
            raise Exception("%d requires > 2 swaps, but it's not supported" % \
            repeated_digit)

    total = 0
    for digit in sorted(special_primes):
        summation = sum(special_primes[digit])
        print "S(%d, %d): %d" % (digits, digit, summation)
        total += summation
    print "Total: %d" % total

if __name__ == '__main__':
    import argparse
    import time

    begin = time.time()

    parser = argparse.ArgumentParser(
        description="Problem 111. URL: http://projecteuler.net/problem=111")
    parser.add_argument('-n', type=int, help="Number of digits to consider.")
    args = vars(parser.parse_args())
    main(args['n'])

    end = time.time()
    print "Runtime: %f seconds." % (end - begin)
