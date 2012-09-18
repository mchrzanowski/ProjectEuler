'''
Created on Sep 17, 2012

@author: mchrzanowski
'''

from operator import mul
from itertools import combinations
from ProjectEulerPrime import ProjectEulerPrime


def main(max_n):

    divisors = dict()

    prime_object = ProjectEulerPrime()

    for n in xrange(2, max_n):

        uniques = set()
        factorization = prime_object.factorize(n)

        for subset_length in xrange(1, len(factorization) + 1):
            for combination in combinations(factorization, subset_length):
                uniques.add(reduce(mul, combination))

        divisors[n] = uniques
        #print "D[%d] = %s" % (n, divisors[n])

    count = 0
    for n in divisors:
        if n + 1 in divisors and len(divisors[n]) == len(divisors[n + 1]):
            count += 1

    print count


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
