'''
Created on Feb 13, 2012

@author: mchrzanowski
'''

import os.path
from time import time

def find_and_replace_key(romanNumeral, dict, currentDecimalValue):
    for key in dict:
        while key in romanNumeral:
            romanNumeral = romanNumeral.replace(key, '', 1)
            currentDecimalValue += dict[key]
    return romanNumeral, currentDecimalValue

def convert_to_decimal(romanNumeral, normalNumeralDict, overrideNumberalDict):
    
    originalNumeral = romanNumeral
    
    # first do a check to determine if one of the special cases exists.
    romanNumeral, decimalNumber = find_and_replace_key(romanNumeral, overrideNumberalDict, 0)
    
    #then check for the normal cases.
    romanNumberal, decimalNumber = find_and_replace_key(romanNumeral, normalNumeralDict, decimalNumber)
    
    return decimalNumber

def convert_to_numeral(decimalNumber, dict):
    newRomanNumeral = ''
    
    # sort the dict number keys from largest to smallest.
    for key, value in sorted(dict.iteritems(), reverse=True):
        while decimalNumber >= key:
            newRomanNumeral = newRomanNumeral + value
            decimalNumber -= key
    
    return newRomanNumeral

def constuct_dicts():
    normalNumeralDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    overrideNumeralDict = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    
    decimalToNumeralDict = {}
    for key in normalNumeralDict:
        decimalToNumeralDict[normalNumeralDict[key]] = key
        
    for key in overrideNumeralDict:
        decimalToNumeralDict[overrideNumeralDict[key]] = key
    
    return normalNumeralDict, overrideNumeralDict, decimalToNumeralDict

def main():
    
    ''' 
        two stages:
        convert the roman number into a decimal number
        convert the decimal number into the most efficient representation of roman numbers
    '''
    start = time()
    
    normalNumeralDict, overrideNumeralDict, decimalToNumeralDict = constuct_dicts()
        
    romanNumerals = open(os.path.join(os.curdir,'./requiredFiles/Problem089RomanNumerals.txt'), 'r')
    
    compressionSavings = 0
    
    for romanNumeral in romanNumerals:
        
        romanNumeral = romanNumeral.strip()
        
        decimalNumber = convert_to_decimal(romanNumeral, normalNumeralDict, overrideNumeralDict)
        
        efficientRomanNumeral = convert_to_numeral(decimalNumber, decimalToNumeralDict)
        
        compressionSavings += len(romanNumeral) - len(efficientRomanNumeral)
    
    print "Compression saved : ", compressionSavings, " bytes."
    
    end = time()
    
    print "Runtime: ", end - start, " seconds."
    

if __name__ == '__main__':
    main()