'''
Created on Sep 20, 2012

@author: mchrzanowski
'''

import Problem135


def main(max_n):

    Problem135.main(max_n, 1)


if __name__ == '__main__':
    import argparse
    import time

    start = time.time()

    parser = argparse.ArgumentParser(
        description="Problem 136. URL: http://projecteuler.net/problem=136")
    parser.add_argument('-n', type=int, help="The max value of n.")
    args = vars(parser.parse_args())
    main(args['n'])

    end = time.time()
    print "Runtime: %f seconds." % (end - start)
