'''
Created on Aug 18, 2012

@author: mchrzanowski
'''

import argparse
import os.path
import time


def main(highest_exponent):

    # http://oeis.org/A003313/b003313.txt
    # provides a list of the smallest number
    # of multiplications required for a given k
    # in n^k
    with open(os.path.join(os.curdir,
        './requiredFiles/Problem122SmallestChains.txt')) as f:
        summation = 0
        for line in f:
            split_line = line.split()
            number = int(split_line[0])
            smallest_chain = int(split_line[1])

            if number <= highest_exponent:
                summation += smallest_chain

        print summation

if __name__ == '__main__':
    begin = time.time()

    parser = argparse.ArgumentParser(
        description="Problem 122. URL: http://projecteuler.net/problem=122")
    parser.add_argument('-max', type=int,
        help="Maximum exponent to calculate the shortest number of" +
        "expontiations")
    args = vars(parser.parse_args())
    main(args['max'])

    end = time.time()
    print "Runtime: %f seconds" % (end - begin)
