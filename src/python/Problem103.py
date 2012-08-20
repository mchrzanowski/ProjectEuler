'''
Created on Aug 19, 2012

@author: mchrzanowski
'''

import Problem105
import time


def main():

    acceptable_groups = list()

    # since n = 6:
    # 11 (middle from n = 5), 18 (11 + 6 + 1),
    # 19 (11 + 9 - 1), 20 (11 + 11 - 2), 22 (11 + 12 - 1),
    # 25 (11 + 13 + 1)

    # I make the guess that n = 7 is in the form of:
    # 20 (middle from n = 6), 31 (20 + 11) +/- 1, 38 (20 + 18) +/- 2,
    # 39 (20 + 19) +/- 3, 40 (20 + 20) +/- 3, 42 (20 + 22) +/- 2,
    # 45 (20 + 25) +/- 1

    # Brute force through all the possibilities to find the optimal set.
    for a in (30, 31, 32):
        for b in (36, 37, 38, 39, 40):
            for c in (36, 37, 38, 39, 40, 41, 42):
                for d in (37, 38, 39, 40, 41, 42, 43):
                    for e in (40, 41, 42, 43, 44):
                        for f in (44, 45, 46):
                            numbers = {20, a, b, c, d, e, f}

                            # no duplicates.
                            if len(numbers) != 7:
                                continue

                            two_subsets_are_equal = False
                            larger_subset_has_larger_sum = True

                            for partition in Problem105.all_partitions(numbers):

                                first, second = partition

                                if Problem105.do_two_subsets_equal_each_other(first, sum(second)):
                                    two_subsets_are_equal = True
                                    break

                            if two_subsets_are_equal:
                                continue

                            for subset in Problem105.all_subsets(numbers):

                                first, second = subset

                                if not Problem105.does_larger_subset_sum_to_a_larger_number(first, second):
                                    larger_subset_has_larger_sum = False
                                    break

                            if not larger_subset_has_larger_sum:
                                continue

                            # both properties have been verified. save this set for later.
                            acceptable_groups.append(numbers)

    # find the set with the smallest sum.
    minimum = None
    for acceptable in acceptable_groups:
        if minimum is None:
            minimum = acceptable
        elif sum(acceptable) < sum(minimum):
            minimum = acceptable

    # print out the set in set string notation as defined by the problem description.
    print "Optimal Set String: %s" % ''.join(str(number) for number in sorted(minimum))


if __name__ == '__main__':
    begin = time.time()
    main()
    end = time.time()
    print "Runtime: %f seconds." % (end - begin)
