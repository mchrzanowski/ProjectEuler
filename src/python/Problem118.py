'''
Created on Sep 12, 2012

@author: mchrzanowski
'''

from itertools import permutations
from ProjectEulerPrime import ProjectEulerPrime


def main():

    # the strategy here is to first find
    # all the primes composed of digits 1-9
    # (with at most one of each digit) and to sort
    # them by size.
    # We then try all the various ways
    # of adding up to 9 by adding variously-sized groups
    # (ie, groups of 1 prime, 2 primes, .... 6 primes)
    # There can only be at most 6 as primes must end with
    # an odd number (thus, 5 numbers), and then there's 2.

    prime_object = ProjectEulerPrime()

    primes_sorted_by_size = dict()

    digits = tuple(str(i) for i in xrange(1, 10))

    for number_length in xrange(1, len(digits) + 1):
        for permutation in permutations(digits, number_length):
            number = int(''.join(permutation))
            if prime_object.isPrime(number):

                if len(permutation) not in primes_sorted_by_size:
                    primes_sorted_by_size[len(permutation)] = set()

                primes_sorted_by_size[len(permutation)].add(tuple(permutation))

    exclusively_prime_groups = 0

    # 1-member groups
    if 9 in primes_sorted_by_size:
        exclusively_prime_groups += len(primes_sorted_by_size[9])

    # 2-member:
    def two_member_good_group_finder(x, y):
        if x + y != 9:
            raise Exception("%d + %d != 9" % (x, y))

        good_groups = set()
        for first in primes_sorted_by_size[x]:
            uniques = set(digit for digit in first)
            for second in primes_sorted_by_size[y]:
                if first == second:
                    continue
                uniques_with_second = set(uniques)
                for digit in second:
                    uniques_with_second.add(digit)

                if len(uniques_with_second) == 9:
                    good_groups.add(frozenset([first, second]))

        return len(good_groups)

    exclusively_prime_groups += two_member_good_group_finder(8, 1)
    exclusively_prime_groups += two_member_good_group_finder(7, 2)
    exclusively_prime_groups += two_member_good_group_finder(6, 3)
    exclusively_prime_groups += two_member_good_group_finder(5, 4)

    # 3-member:
    def three_member_good_group_finder(x, y, z):

        if x + y + z != 9:
            raise Exception("%d + %d + %d != 9" % (x, y, z))

        good_groups = set()
        for first in primes_sorted_by_size[x]:
            uniques = set(digit for digit in first)
            for second in primes_sorted_by_size[y]:
                if first == second:
                    continue

                uniques_with_second = set(uniques)
                for digit in second:
                    uniques_with_second.add(digit)
                for third in primes_sorted_by_size[z]:
                    if third == second or third == first:
                        continue

                    all_uniques = set(uniques_with_second)
                    for digit in third:
                        all_uniques.add(digit)

                    if len(all_uniques) == 9:
                        good_groups.add(frozenset([first, second, third]))

        return len(good_groups)

    exclusively_prime_groups += three_member_good_group_finder(7, 1, 1)
    exclusively_prime_groups += three_member_good_group_finder(6, 2, 1)
    exclusively_prime_groups += three_member_good_group_finder(5, 3, 1)
    exclusively_prime_groups += three_member_good_group_finder(5, 2, 2)
    exclusively_prime_groups += three_member_good_group_finder(4, 3, 2)
    exclusively_prime_groups += three_member_good_group_finder(4, 4, 1)
    exclusively_prime_groups += three_member_good_group_finder(3, 3, 3)

    # 4-member:
    def four_member_good_group_finder(x, y, z, xx):

        if x + y + z + xx != 9:
            raise Exception("%d + %d + %d + %d != 9" % (x, y, z, xx))

        good_groups = set()
        for first in primes_sorted_by_size[x]:
            uniques = set(digit for digit in first)
            for second in primes_sorted_by_size[y]:
                if first == second:
                    continue

                uniques_with_second = set(uniques)
                for digit in second:
                    uniques_with_second.add(digit)
                for third in primes_sorted_by_size[z]:
                    if third == second or third == first:
                        continue

                    uniques_with_third = set(uniques_with_second)
                    for digit in third:
                        uniques_with_third.add(digit)

                    for fourth in primes_sorted_by_size[xx]:
                        if fourth == third or fourth == second or \
                        fourth == first:
                            continue

                        all_uniques = set(uniques_with_third)
                        for digit in fourth:
                            all_uniques.add(digit)

                        if len(all_uniques) == 9:
                            good_groups.add(frozenset([first, second, third,
                            fourth]))

        return len(good_groups)

    exclusively_prime_groups += four_member_good_group_finder(6, 1, 1, 1)
    exclusively_prime_groups += four_member_good_group_finder(5, 2, 1, 1)
    exclusively_prime_groups += four_member_good_group_finder(4, 2, 2, 1)
    exclusively_prime_groups += four_member_good_group_finder(4, 3, 1, 1)
    exclusively_prime_groups += four_member_good_group_finder(3, 3, 2, 1)
    exclusively_prime_groups += four_member_good_group_finder(3, 2, 2, 2)

    # 5-member:
    def five_member_good_group_finder(x, y, z, xx, yy):

        if x + y + z + xx + yy != 9:
            raise Exception("%d + %d + %d + %d + %d != 9" % (x, y, z, xx, yy))

        good_groups = set()
        for first in primes_sorted_by_size[x]:
            uniques = set(digit for digit in first)
            for second in primes_sorted_by_size[y]:
                if first == second:
                    continue

                uniques_with_second = set(uniques)
                for digit in second:
                    uniques_with_second.add(digit)
                for third in primes_sorted_by_size[z]:
                    if third == second or third == first:
                        continue

                    uniques_with_third = set(uniques_with_second)
                    for digit in third:
                        uniques_with_third.add(digit)

                    for fourth in primes_sorted_by_size[xx]:
                        if fourth == third or fourth == second or \
                        fourth == first:
                            continue

                        uniques_with_fourth = set(uniques_with_third)
                        for digit in fourth:
                            uniques_with_fourth.add(digit)

                        for fifth in primes_sorted_by_size[yy]:
                            if fifth == first or fifth == second or \
                            fifth == third or fifth == fourth:
                                continue

                            all_uniques = set(uniques_with_fourth)
                            for digit in fifth:
                                all_uniques.add(digit)

                            if len(all_uniques) == 9:
                                good_groups.add(frozenset([first, second,
                                third, fourth, fifth]))

        return len(good_groups)

    exclusively_prime_groups += five_member_good_group_finder(5, 1, 1, 1, 1)
    exclusively_prime_groups += five_member_good_group_finder(4, 2, 1, 1, 1)
    exclusively_prime_groups += five_member_good_group_finder(3, 3, 1, 1, 1)
    exclusively_prime_groups += five_member_good_group_finder(3, 2, 2, 1, 1)
    exclusively_prime_groups += five_member_good_group_finder(2, 2, 2, 2, 1)

    # 6-member
    def six_member_good_group_finder(x, y, z, xx, yy, zz):

        if x + y + z + xx + yy + zz != 9:
            raise Exception("%d + %d + %d + %d + %d != 9" %
            (x, y, z, xx, yy, zz))

        good_groups = set()
        for first in primes_sorted_by_size[x]:
            uniques = set(digit for digit in first)
            for second in primes_sorted_by_size[y]:
                if first == second:
                    continue

                uniques_with_second = set(uniques)
                for digit in second:
                    uniques_with_second.add(digit)
                for third in primes_sorted_by_size[z]:
                    if third == second or third == first:
                        continue

                    uniques_with_third = set(uniques_with_second)
                    for digit in third:
                        uniques_with_third.add(digit)

                    for fourth in primes_sorted_by_size[xx]:
                        if fourth == third or fourth == second or \
                        fourth == first:
                            continue

                        uniques_with_fourth = set(uniques_with_third)
                        for digit in fourth:
                            uniques_with_fourth.add(digit)

                        for fifth in primes_sorted_by_size[yy]:
                            if fifth == first or fifth == second or \
                            fifth == third or fifth == fourth:
                                continue

                            uniques_with_fifth = set(uniques_with_fourth)
                            for digit in fifth:
                                uniques_with_fifth.add(digit)

                            for sixth in primes_sorted_by_size[zz]:
                                if sixth == first or sixth == second or \
                                sixth == third or sixth == fourth or \
                                sixth == fifth:
                                    continue

                                all_uniques = set(uniques_with_fifth)
                                for digit in sixth:
                                    all_uniques.add(digit)

                                if len(all_uniques) == 9:
                                    good_groups.add(frozenset([first, second,
                                    third, fourth, fifth, sixth]))

        return len(good_groups)

    exclusively_prime_groups += six_member_good_group_finder(2, 2, 2, 1, 1, 1)
    exclusively_prime_groups += six_member_good_group_finder(2, 3, 1, 1, 1, 1)

    print "Number of groups: %d" % exclusively_prime_groups

if __name__ == '__main__':
    import time

    start = time.time()
    main()
    end = time.time()
    print "Runtime: %f seconds" % (end - start)
