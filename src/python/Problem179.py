'''
Created on Sep 17, 2012

@author: mchrzanowski
'''

from collections import Counter
from ProjectEulerPrime import ProjectEulerPrime


def main(max_n):

    divisors = dict()

    prime_object = ProjectEulerPrime()

    for n in xrange(max_n, 1, -1):

        # from:
        # http://stackoverflow.com/questions/110344/algorithm-to-
        # calculate-the-number-of-divisors-of-a-given-number

        # we know that:
        # divisors(n) = product(each factor's multiplicity + 1)

        factorization = prime_object.factorize(n)

        multiplicities = Counter(factorization)

        divisors[n] = 1

        for factor in multiplicities:
            divisors[n] *= multiplicities[factor] + 1

    count = 0
    for n in divisors:
        if n + 1 in divisors and divisors[n] == divisors[n + 1]:
            count += 1

    print "Adjacent pairs with the same number of divisors: %d" % count


if __name__ == '__main__':
    import argparse
    import time

    start = time.time()

    parser = argparse.ArgumentParser(
        description="Problem 179. URL: http://projecteuler.net/problem=179")
    parser.add_argument('-n', type=int,
        help="The max value of n.")
    args = vars(parser.parse_args())
    main(args['n'])

    end = time.time()
    print "Runtime: %f seconds." % (end - start)
