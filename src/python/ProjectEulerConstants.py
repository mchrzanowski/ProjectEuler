'''
Created on Jan 19, 2012

@author: mchrzanowski
'''
    
def isPrime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

def isNumberPalindromic(number):
    ''' check if number is a palindrome '''
    number = str(number)
    if number[: len(number) / 2] == number[:: -1][: len(number) / 2]:
            return True
    return False

def isNumberPandigital(number, lastNumberToVerify = 9, includeZero = False):
    ''' check if number is pandigital '''
    
    numberLimit = lastNumberToVerify
    if includeZero:
        startingNumber = 0
        numberLimit += 1
    else:
        startingNumber = 1
    
    number = str(number)
    
    if len(number) != numberLimit:
        return False 
    
    listOfNumbers = [char for char in number]
    for i in xrange(startingNumber, lastNumberToVerify + 1):
        stringifiedNumber = str(i)
        if stringifiedNumber in listOfNumbers:
            listOfNumbers.remove(stringifiedNumber)
        else:
            return False
        
    if len(listOfNumbers) == 0:
        return True
    else:
        return False
    
    
    
    