'''
Created on Jan 11, 2012

@author: mchrzanowski
'''

__LIMIT = 999999  # as 999999 > 6 * 9 ^ 5 , this is our ceiling.
__POWER = 5

def main():
    winners = set([])
    for number in xrange(2, __LIMIT): # exclude 1 as it's not a sum (but would qualify)
        numberString = str(number)
        addedValue = 0
        for numeral in numberString:
            addedValue = addedValue + int(numeral) ** __POWER
        if addedValue == number:
            winners.add(number)
    print "Numbers: ", winners
    print "Sum: ", sum(winners)

if __name__ == '__main__':
    main()