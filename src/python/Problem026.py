'''
Created on Jan 8, 2012

@author: mchrzanowski
'''

from decimal import getcontext, Decimal
from time import time

def main():
    start = time()
    getcontext().prec = 5000
    maxLength = ""
    position = -1
    for i in range(2, 1000):
        numString = str(Decimal(1.) / Decimal(i))[2:]
#        print "Current Number: " + "1 / " + str(i) + " : " + numString
        cycle = detectRecurringCycle(numString)
        if cycle is not None and len(cycle) > len(maxLength):
            maxLength = cycle
            position = i
#            print "New longest cycle: " , maxLength , "\t: Start: " , i
    end = time()

    print "Longest cycle: " , maxLength 
    print "Start: " , position
    print "Size: " , len(maxLength)
    print "Time: " , int(end - start) , " s."


def detectRecurringCycle(s):
    longestCycle = ""
    for i in range(0, len(s)):
        for j in range(i, len(s)):
            if i == j:
                keyToCheck = s[j]
            else:
                keyToCheck = s[i:j+1]
            sToPass = s[j+1:]
            if checkIfCycle(keyToCheck, sToPass):
                if checkIfSuperSet(keyToCheck, longestCycle):
                    return longestCycle
                else:
                    longestCycle = keyToCheck
                    
def checkIfSuperSet(contender, incumbent):
    if contender.startswith(incumbent):
        contender = contender[len(incumbent):]
    if incumbent.startswith(contender):
        return True # this is just the cycle recurring. forget it!
    else:
        return False    # this is a new portion of the series. keep it!
    
    
def checkIfCycle(keyToCheck, s):
    if s.startswith(keyToCheck):
#        print "Cycle found. Key: " + keyToCheck + " subS: " + s
        return True
    else:
        return False
    

if __name__ == '__main__':
    main()    
