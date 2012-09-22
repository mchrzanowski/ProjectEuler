'''
Created on Sep 20, 2012

@author: mchrzanowski
'''


def produce_n(z, k):
    return 2 * k * z + 3 * k ** 2 - z ** 2


def main(max_n, solution_number):

    solutions = dict()

    # we can write x ** 2 - y ** 2 - z ** 2 = n as:
    # (z + 2 * k) ** 2 - (z + k) ** 2 - z ** 2 == n

    # if you find the partial derivative with respect
    # to z, you see that z = k is the maximum value of the
    # function. Furthermore, if you look at the output for small k,
    # you see that the function is symmetric about the maximum:
    #   k=2, z=1, n=15
    #   k=2, z=2, n=16
    #   k=2, z=3, n=15
    #   k=2, z=4, n=12
    #   k=2, z=5, n=7
    #   k=2, z=6, n=0
    #   k=3, z=1, n=32
    #   k=3, z=2, n=35
    #   k=3, z=3, n=36
    #   k=3, z=4, n=35
    #   k=3, z=5, n=32
    #   k=3, z=6, n=27
    #   k=3, z=7, n=20
    #   k=3, z=8, n=11
    #   k=3, z=9, n=0
    # Finally, note that the last z value before n = 0 is, for a k:
    # last_z = 2 + 3 * (k - 1)
    # Therefore, the strategy is to count from last_z to
    # k. We cache the n values up until then. If
    # n is >= max_n along the way, we stop and increment k.
    # We have finished once the last value of z for a given k is >= max_n.

    last_z_is_larger_than_or_equal_to_max_n = False
    k = 1
    while not last_z_is_larger_than_or_equal_to_max_n:

        for z in xrange(2 + 3 * (k - 1), k - 1, -1):

            n = produce_n(z, k)

            if n >= max_n:
                if z == 2 + (k - 1) * 3:
                    last_z_is_larger_than_or_equal_to_max_n = True
                break

            if n not in solutions:
                solutions[n] = 0

            if z > k and z <= 2 * k - 1:
                solutions[n] += 2
            else:
                solutions[n] += 1

        k += 1

    valuable_keys = 0
    for key in solutions:
        if solutions[key] == solution_number:
            valuable_keys += 1

    print "Values of n < %d that have %d solutions: %d" % \
    (max_n, solution_number, valuable_keys)


if __name__ == '__main__':
    import argparse
    import time

    start = time.time()

    parser = argparse.ArgumentParser(
        description="Problem 135. URL: http://projecteuler.net/problem=135")
    parser.add_argument('-n', type=int, help="The max value of n.")
    parser.add_argument('-s', type=int, help="# of solutions to look for.")
    args = vars(parser.parse_args())
    main(args['n'], args['s'])

    end = time.time()
    print "Runtime: %f seconds." % (end - start)
