'''
Created on Apr 7, 2012

@author: mchrzanowski
'''

from time import time

def calculateIncreaingNumbers(limit):
    
    def getDefaults():
        defaults = {}
        for i in xrange(1, 10):
            defaults[i] = 10 - i
        return defaults
    
    combinationDict = getDefaults()
    
    totalNumbers = sum(combinationDict.values())
    
    for iteration in xrange(1, limit - 1):
        for mutatingKey in sorted(combinationDict.keys()):
            combinationDict[mutatingKey] = sum(combinationDict[key] for key in combinationDict if key >= mutatingKey)
            totalNumbers += combinationDict[mutatingKey]
     
    return totalNumbers

def calculateDecreasingNumbers(limit):
    
    def getDefaults():
        defaults = {}
        for i in xrange(0, 10):
            defaults[i] = i + 1
        return defaults
    
    combinationDict = getDefaults()
    
    totalNumbers = sum(combinationDict.values())
    
    for iteration in xrange(1, limit - 1):
        for j in sorted(combinationDict.keys(), reverse = True):
            combinationDict[j] = sum(combinationDict[key] for key in combinationDict if key <= j)
            totalNumbers += combinationDict[j] - 1
    
    return totalNumbers
    

def main():
    
    DIGITS = 100
    
    increatingNumbers = calculateIncreaingNumbers(DIGITS)
    decreaingNumber = calculateDecreasingNumbers(DIGITS)
    
    print increatingNumbers, decreaingNumber
    print increatingNumbers + decreaingNumber - 1

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."
