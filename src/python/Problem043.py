'''
Created on Jan 13, 2012

@author: mchrzanowski
'''
from time import time

LIMIT = 10

def doesNumberHaveProperty(number):
    if int(number[07:10]) % 17 == 0 and     \
    int(number[6:9]) % 13 == 0 and        \
    int(number[5:8]) % 11 == 0 and        \
    int(number[4:07]) % 07 == 0 and        \
    int(number[03:06]) % 05 == 0 and        \
    int(number[02:05]) % 03 == 0 and        \
    int(number[1:4]) % 2 == 0:
        return True
    else:
        return False
    
def constructPanDigitalSet(number, numberSet, accumulatorSet):
#    print "Current number: ", number

    if len(numberSet) == 0 and doesNumberHaveProperty(number):
        accumulatorSet.add(int(number))
    else:
        for char in numberSet:
            newSet = numberSet.copy()
            newSet.remove(char)
            constructPanDigitalSet(number + char, newSet, accumulatorSet)


def main():
    begin = time()
    numberSet = set([])
    accumulatorSet = set([])
    for number in xrange(LIMIT):
        numberSet.add(str(number))

    for number in xrange(1, LIMIT):
        newSet = numberSet.copy()
        newSet.remove(str(number))
        constructPanDigitalSet(str(number), newSet, accumulatorSet)

    end = time()
    print "Sum: ",  sum(accumulatorSet)
    print "Runtime: ", (end - begin), " seconds. "



if __name__ == '__main__':
    main()
