'''
Created on Sep 14, 2012

@author: mchrzanowski
'''

from Problem173 import construct_laminae_frequency


def main(tile_limit, lower_n_bound, upper_n_bound):

    # first, construct L(n) -> #
    L = construct_laminae_frequency(tile_limit)

    # now, build N(#)
    N = dict()
    for number_of_tiles in L:
        number_of_laminae = L[number_of_tiles]
        if number_of_laminae not in N:
            N[number_of_laminae] = 0
        N[number_of_laminae] += 1

    print "Sum(N(n)), %d <= n <= %d: %d" % \
    (lower_n_bound, upper_n_bound, \
    sum(N[number_of_laminae] for number_of_laminae in \
    xrange(lower_n_bound, upper_n_bound + 1)))

if __name__ == '__main__':
    import argparse
    import time

    start = time.time()

    parser = argparse.ArgumentParser(
        description="Problem 174. URL: http://projecteuler.net/problem=174")
    parser.add_argument('-t', type=int, help="Maximum tile count.")
    parser.add_argument('-l', type=int, help="Lower bound on n in N(n).")
    parser.add_argument('-u', type=int, help="Upper bound on n in N(n).")
    args = vars(parser.parse_args())
    main(args['t'], args['l'], args['u'])

    end = time.time()
    print "Runtime: %f seconds." % (end - start)
