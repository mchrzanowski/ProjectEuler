'''
Created on Aug 18, 2012

@author: mchrzanowski
'''

import itertools
import os.path
import time


def do_two_subsets_equal_each_other(numbers, value_to_equal):
    '''
        exact subset problem.
        return true if we have a subset that equals value_to_equal.
        http://www.cs.dartmouth.edu/~ac/Teach/CS105-Winter05/Notes/nanda-scribe-3.pdf
    '''

    def merge_lists(first, second):
        return first + second

    def add_to_every_element(value_to_add, elements):
        return map(lambda x: x + value_to_add, elements)

    L = [[0]]
    numbers = list(numbers)  # we need to preserve position.
    numbers.insert(0, 0)     # we need a header for the below algo.

    for i in xrange(1, len(numbers)):
        L.append(list())

        raw_list = merge_lists(L[i - 1],
            add_to_every_element(numbers[i], L[i - 1]))

        for element in raw_list:
            if value_to_equal == element:
                return True
            elif element < value_to_equal:
                L[i].append(element)

    return False


def does_larger_subset_sum_to_a_larger_number(B, C):
    '''
        for any two subsets B & C, if len(B) > len(C),
        then sum(B) > sum(C). otherwise, return False
    '''

    if len(B) > len(C) and sum(B) <= sum(C):
        return False

    if len(C) > len(B) and sum(C) <= sum(B):
        return False

    return True


def all_subsets(numbers):
    '''
        return a set of sets, each containing
        two subsets of this number collection
    '''
    subsets = set()
    for first_length in xrange(1, len(numbers)):
        for first_combo in itertools.combinations(numbers, first_length):
            disjoint_numbers = [number for number in numbers if number not in first_combo]
            for second_length in xrange(1, len(disjoint_numbers) + 1):
                for second_combo in itertools.combinations(disjoint_numbers, second_length):
                    subsets.add(frozenset((first_combo, second_combo,)))

    return subsets


def all_partitions(numbers):
    '''
        return a list of tuples, each containing all the various
        partitions of this number collection
    '''
    partitions = list()
    for length in xrange(1, len(numbers)):
        for combination in itertools.combinations(numbers, length):
            numbers_sans_combination = [element for element in numbers if element not in combination]
            partitions.append((numbers_sans_combination, combination))

    return partitions


def main():

    with open(os.path.join(os.curdir,
        './requiredFiles/Problem105Sets.txt')) as f:

        special_sets = list()
        for row in f:
            numbers = set()
            for number in row.split(","):
                numbers.add(int(number))

            two_subsets_are_equal = False
            larger_subset_has_larger_sum = True

            for partition in all_partitions(numbers):

                first, second = partition

                if do_two_subsets_equal_each_other(first, sum(second)):
                    two_subsets_are_equal = True
                    break

            if two_subsets_are_equal:
                continue

            for subset in all_subsets(numbers):

                first, second = subset

                if not does_larger_subset_sum_to_a_larger_number(first, second):
                    larger_subset_has_larger_sum = False
                    break

            if not larger_subset_has_larger_sum:
                continue

            special_sets.append(numbers)

        total = sum(sum(special_set) for special_set in special_sets)
        print "Total: %d" % total


if __name__ == '__main__':
    begin = time.time()
    main()
    end = time.time()
    print "Runtime: %f seconds." % (end - begin)
