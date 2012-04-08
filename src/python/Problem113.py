'''
Created on Apr 7, 2012

@author: mchrzanowski
'''

from operator import ge, le
from time import time

def calculateBouncyNumbers(limit):
    
    ''' 
    there are two sets of bouncy numbers:
        1). numbers that are stable or decreasing
        2). numbers that are stable or increasing
    there exists an non-empty intersection between these two sets: it's [# of digits] * 9 .
    but we don't want to use sets because that's lame and slow.
    we calculate all unique bouncies for one type at a time.
    we then add back the duplicate bouncies.
    '''
    
    increasingNumbers = calculateUniqueNumbersInOneDirection(limit = limit, goingForward = True)
    decreasingNumbers = calculateUniqueNumbersInOneDirection(limit = limit, goingForward = False)
    
    return increasingNumbers + decreasingNumbers + 9 * limit
    

def calculateUniqueNumbersInOneDirection(limit, goingForward):
    
    ''' 
    the basic idea here is that for a number that is n digits long,
    the number of bouncies is a function of the number of bouncies for numbers n - 1 digits long.
    the numbers that we look at that are n - 1 digits long depend on whether we are going forward or not
    this means that we are at most keeping track of bouncy numbers based on their starting digit.
    
    if we're going forward, we care about the bouncies for all n - 1 digits that started with a number ge to a given value from 1-9
    if backwards, we care about all bounces that started with a number le to a given value.
    '''
    
    def getDefaults():
        ''' 
        return a dict representing the starting number of bouncies for 1-9. 
        this is all natural numbers < 10, and so return a dict of keys pointing to 1
        '''
        defaults = {}
                
        if goingForward:                # increasing numbers never have a zero. but zeros are vital for decreasing numbers.
            startingValue = 1 
        else: 
            startingValue = 0
        
        for i in xrange(startingValue, 10):
            defaults[i] = 1
        
        return defaults
    
    combinationDict = getDefaults()
    totalNumbers = 0                    # don't include the 1-digit bouncies as they are non-unique.
    
    if goingForward:                    # for the comparisons in the loop.
        operator = ge
    else:
        operator = le
    
    for iteration in xrange(1, limit):
        for mutatingKey in sorted(combinationDict.keys(), reverse = not goingForward):
            combinationDict[mutatingKey] = sum(combinationDict[key] for key in combinationDict if operator(key, mutatingKey))
            totalNumbers += combinationDict[mutatingKey] - 1    # remove one to account for the repeating digit case
    
    return totalNumbers

def main():
    
    DIGITS = 100
    
    print calculateBouncyNumbers(DIGITS)

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."
