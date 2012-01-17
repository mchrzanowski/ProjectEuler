'''
Created on Jan 16, 2012

@author: mchrzanowski
'''

from time import time

YEAR_LIMIT = 2001
YEAR_BASE = 1900

daysInMonth = {
               1: 31,
               2: 28,
               3: 31,
               4: 30,
               5: 31,
               6: 30,
               7: 31,
               8: 31,
               9: 30,
               10: 31,
               11: 30,
               12: 31
}

def main():
    
    start = time()
    
    runningDayCounter = 1
    sundayCount = 0
    for year in xrange(YEAR_BASE, YEAR_LIMIT):
        for month in xrange(1, len(daysInMonth) + 1):
            
            if year > YEAR_BASE and runningDayCounter % 7 is 0:
                sundayCount += 1
           
            runningDayCounter += daysInMonth[month]
            
            # leap years occur in years divisible by 4 and, for centuries, only when divisible by 400
            if month == 2 and year % 4 is 0:
                if year % 100 is not 0:
                    runningDayCounter += 1
                elif year % 400 is 0:
                    runningDayCounter += 1   
                
    
    end = time()
            
    print "Sunday Count: ", sundayCount
    print "Runtime: ", end - start, " seconds."


if __name__ == '__main__':
    main()