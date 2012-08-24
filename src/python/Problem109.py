'''
Created on Aug 23, 2012

@author: mchrzanowski
'''


def main(max_score):

    # map a zone to its quantitative value.
    number_to_zones = {
        0: {'S0'}, 1: {'S1'}, 2: {'D1', 'S2'}, 3: {'S3', 'T1'},
        4: {'S4', 'D2'}, 5: {'S5'}, 6: {'T2', 'D3', 'S6'}, 7: {'S7'},
        8: {'S8', 'D4'}, 9: {'S9', 'T3'}, 10: {'S10', 'D5'}, 11: {'S11'},
        12: {'S12', 'T4', 'D6'}, 13: {'S13'}, 14: {'S14', 'D7'},
        15: {'S15', 'T5'}, 16: {'S16', 'D8'}, 17: {'S17'},
        18: {'S18', 'D9', 'T6'}, 19: {'S19'}, 20: {'S20', 'D10'}, 21: {'T7'},
        22: {'D11'}, 24: {'T8', 'D12'}, 25: {'S25'}, 26: {'D13'}, 27: {'T9'},
        28: {'D14'}, 30: {'T10', 'D15'}, 32: {'D16'}, 33: {'T11'}, 34: {'D17'},
        36: {'D18', 'T12'}, 38: {'D19'}, 39: {'T13'}, 40: {'D20'},
        42: {'T14'}, 45: {'T15'}, 48: {'T16'}, 50: {'D25'}, 51: {'T17'},
        54: {'T18'}, 57: {'T19'},
        60: {'T20'},
    }

    # create a set of all the values of doubles.
    # this means all even numbers from 2 to 40 as well as 50.
    doubles = set(value for value in xrange(2, 40 + 1, 2))
    doubles.add(50)

    distinct_sequences = set()

    # first, get the last value. it has to be a double, meaning it's
    # confined to the range 2..40, 50
    for last_dart_value in doubles:
        # now, go through all possible numerical values for the first dart.
        for first_dart_value in number_to_zones:
            # ditto for the second.
            for second_dart_value in number_to_zones:

                if last_dart_value + first_dart_value + \
                second_dart_value > max_score:
                    continue

                # now go through each zone. this is necessary as multiple
                # sequences containing the same zones (sans the last value)
                # are not considered unique.
                for first_zone in number_to_zones[first_dart_value]:
                    for second_zone in number_to_zones[second_dart_value]:
                        sequence = [first_zone, second_zone]
                        # sorting guarantees uniqueness.
                        sequence.sort()
                        sequence.append(last_dart_value)
                        distinct_sequences.add(tuple(sequence))

    print "Distinct ways of checking out with a score less than %d: %d" % \
        (max_score, len(distinct_sequences))

if __name__ == '__main__':
    import argparse
    import time

    begin = time.time()

    parser = argparse.ArgumentParser(
        description="Problem 109. URL: http://projecteuler.net/problem=109")
    parser.add_argument('-max_score', type=int,
        help="Max score from which to checkout from.")
    args = vars(parser.parse_args())
    main(args['max_score'])

    end = time.time()
    print "Runtime: %f seconds." % (end - begin)
