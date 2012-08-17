'''
Created on Aug 16, 2012

@author: mchrzanowski
'''

from __future__ import division

import argparse
import itertools
import operator
import time


def main(turns):

    # Examples of probabilities from the trials:
    # If we get all Blues: (1/2) * (1/3) * ....
    # If we get all Reds: (1/2) * (2/3) * ...

    # create the denominator. this is just the number of disks
    # we deal with for any given sequence of trials multiplied.
    common_denominator = reduce(operator.mul,
        [number for number in xrange(2, 2 + turns)])

    numerator = 0

    for product in itertools.product('BR', repeat=turns):

        # look for those patterns which have too few Bs
        # if so, continue
        number_of_Bs = len(filter(lambda letter: letter == 'B', product))
        if number_of_Bs <= turns // 2:
            continue

        # to create the numerator, note that the probability of getting a 'B'
        # in any trial will always be 1/N and 'R' is (N-1)/N.
        # Since we know ahead of time
        # what the denominator is going to be after all the trials, we just
        # need to multiply all the non-one numerators together.
        product_numerator = 1
        for index, letter in enumerate(product):
            if letter == 'R':
                product_numerator *= index + 1

        numerator += product_numerator

    # Now, to get the max prize to assign,
    # we want to do 1/(probability of winning)
    print "Max Prize: %d" % (common_denominator / numerator)

if __name__ == '__main__':
    begin = time.time()

    parser = argparse.ArgumentParser(
        description="Problem 121. URL: http://projecteuler.net/problem=121")
    parser.add_argument('-trials', type=int, help="Number of trials")
    args = vars(parser.parse_args())
    main(args['trials'])

    end = time.time()
    print "Runtime: %f seconds" % (end - begin)
