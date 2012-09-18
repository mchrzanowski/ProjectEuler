'''
Created on Sep 15, 2012

@author: mchrzanowski
'''


def main(value_to_exceed):
    # empirical analysis suggests that the n
    # that produces an A(n) greater than the value
    # we're interested in is slightly above the value itself.
    # for instance:
    # 10: A[17] = 16
    # 100: A[109] = 108
    # 100: A[1017] = 1008
    # 1000: A[10007] = 10006
    # the general algo is therefore to start finding mappings
    # for n starting at the passed-in value by iterating through
    # progressively larger repunits until we find a match.

    A = dict()

    factor = value_to_exceed

    while True:

        if factor & 1 == 1 and factor % 5 != 0:

            repunit_length = 2
            while factor not in A:

                # from p132, a repunit is formed by:
                # a base-10 repunit is formed via the following forumula:
                # (10 ** (number of digits) - 1) / (10 - 1)

                # we use modular exponentiation to see whether
                # 10 ** (number of digits) is divisible by 9 * some prime
                # with remainder 1.

                if pow(10, repunit_length, 9 * factor) == 1:
                    A[factor] = repunit_length

                repunit_length += 1

            if A[factor] > value_to_exceed:
                print "A[%d] = %d" % (factor, A[factor])
                break

        factor += 1


if __name__ == '__main__':
    import argparse
    import time

    start = time.time()

    parser = argparse.ArgumentParser(
        description="Problem 129. URL: http://projecteuler.net/problem=129")
    parser.add_argument('-v', type=int,
        help="The value that A(n) should exceed.")
    args = vars(parser.parse_args())
    main(args['v'])

    end = time.time()
    print "Runtime: %f seconds." % (end - start)
