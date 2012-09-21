'''
Created on Sep 20, 2012

@author: mchrzanowski
'''


def produce_n(z, k):
    return 2 * k * z + 3 * k ** 2 - z ** 2


def main(max_n, solution_number):

    solutions = dict()

    k = 1
    while True:

        last_z = 2 + (k - 1) * 3

        if produce_n(last_z, k) >= max_n:
            break

        z = 1

        while True:

            n = produce_n(z, k)

            #print "k=%d, z=%d, n=%d" % (k, z, n)

            if n <= 0:
                break

            if n < max_n:
                if n not in solutions:
                    solutions[n] = 1
                else:
                    solutions[n] += 1

            z += 1
        k += 1

    valuable_keys = set()
    for key in solutions:
        if solutions[key] == solution_number:
            valuable_keys.add(key)

    print len(valuable_keys)


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
