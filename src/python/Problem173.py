'''
Created on Aug 24, 2012

@author: mchrzanowski
'''


def constuct_laminae_frequency(tile_limit):
    ''' return a dict where:
        key = number of tiles
        value = number of different laminae formed
    '''
    laminae_frequency = dict()

    # the smallest hole is a single square (1 ** 2)
    hole_side = 1

    while True:

        # for any given hole, the square that supports it
        # is the next odd or even number (depending on the hole size itself)
        square_side = hole_side + 2
        tiles = square_side ** 2 - hole_side ** 2

        while tiles <= tile_limit:
            if tiles not in laminae_frequency:
                laminae_frequency[tiles] = 1
            else:
                laminae_frequency[tiles] += 1
            square_side += 2
            tiles = square_side ** 2 - hole_side ** 2

        # did we manage to not increment square_side once?
        # then we are done.
        if square_side == hole_side + 2:
            break
        else:
            hole_side += 1

    return laminae_frequency


def main(tile_limit):
    # the strategy is to create all possible holes
    # and to then construct every possible square that could support
    # such a hole given the limit on the number of tiles.

    laminae_frequency = constuct_laminae_frequency(tile_limit)

    print "Unique square laminae: %d" % \
        sum(laminae_frequency[tile_size] for tile_size in laminae_frequency)

if __name__ == '__main__':
    import argparse
    import time

    start = time.time()

    parser = argparse.ArgumentParser(
        description="Problem 173. URL: http://projecteuler.net/problem=173")
    parser.add_argument('-max', type=int, help="Maximum tile count.")
    args = vars(parser.parse_args())
    main(args['max'])

    end = time.time()
    print "Runtime: %f seconds." % (end - start)
