'''
Created on Aug 20, 2012

@author: mchrzanowski
'''

import argparse
import Problem105
import time


def main(n_value):

    numbers = [number for number in xrange(1, n_value + 1)]

    groups_to_check_for_equality = 0

    for subset in Problem105.all_subsets(numbers):

        first_subset, second_subset = subset

        # because we assume that the second rule has been met,
        # we can assume that two differently-sized subsets
        # cannot possibly be equal
        if len(first_subset) != len(second_subset):
            continue

        # since the sequence is strictly increasing, no two
        # sets of cardinality 1 can be equal.
        if len(first_subset) == 1:
            continue

        # to see whether we need to test for equality,
        # we compare the values at the same indicies in both subsets.
        # if subset A's values are all less than subset B's counterparts,
        # then clearly there is no need to test for equality.
        smaller = 0
        greater = 0
        for pair in zip(first_subset, second_subset):
            first, second = pair
            if first < second:
                smaller += 1
            else:
                greater += 1

        if smaller == len(first_subset) or greater == len(first_subset):
            continue

        # these are the ones that have survived and need further processing.
        groups_to_check_for_equality += 1

    print "Groups to check for equality: %d" % groups_to_check_for_equality

if __name__ == '__main__':
    begin = time.time()

    parser = argparse.ArgumentParser(
        description="Problem 106. URL: http://projecteuler.net/problem=106")
    parser.add_argument('-n', type=int,
        help="Number of elements in the set. Corresponds to the " +
        "'n' value in the problem")
    args = vars(parser.parse_args())
    main(args['n'])

    end = time.time()
    print "Runtime: %f seconds." % (end - begin)
