'''
Created on Jan 19, 2012

@author: mchrzanowski
'''

from ProjectEulerPrime import ProjectEulerPrime
import sys

def getListOfPrimes(numberOfPrimesToGet):
    ''' get a list of primes of length numberOfPrimesToGet '''
    primeList = []
    
    if numberOfPrimesToGet <= 0:
        return primeList
    
    primeList.append(2)     # numberOfPrimesToGet has to be at least 1 at this point.
    
    candidate = 3
    while len(primeList) != numberOfPrimesToGet :
        if isPrime(candidate):
            primeList.append(candidate)
        candidate += 2
    
    return primeList
    
def isPrime(n):
    '''
    check if integer n is a prime
    from: http://www.daniweb.com/software-development/python/code/216880
    '''
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

def isNumberPandigital(number, lastNumberToVerify=9, includeZero=False):
    ''' check if number is pandigital '''
    
    numberLimit = lastNumberToVerify
    if includeZero:
        startingNumber = 0
        numberLimit += 1
    else:
        startingNumber = 1
    
    number = str(int(number))       # convert to int to get rid of initial zeroes. then convert to string.
    
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
    
def generatePentagonalNumbers(numberLimit, startingNumber=1):
    ''' generator that produces pentagonal numbers for 1..numberLimit '''
    for i in xrange(startingNumber, numberLimit + 1):
        yield i * (3 * i - 1) / 2    

def generateHexagonalNumbers(numberLimit, startingNumber=1):
    ''' generator that produces hexagonal numbers for 1..numberLimit '''
    for i in xrange(startingNumber, numberLimit + 1):
        yield i * (2 * i - 1)
        
def generateTriangleNumbers(numberLimit, startingNumber=1): 
    ''' generator that produces triangle numbers for 1..numberLimit '''
    for i in xrange(startingNumber, numberLimit + 1):
        yield i * (i + 1) / 2   

def generateOctagonalNumbers(numberLimit, startingNumber=1):
    ''' generator that produces octagonal numbers for 1..numberLimit '''
    for i in xrange(startingNumber, numberLimit + 1):
        yield i * (3 * i - 2)

def generateHeptagonalNumbers(numberLimit, startingNumber=1):
    ''' generator that produces heptagonal numbers for 1..numberLimit '''
    for i in xrange(startingNumber, numberLimit + 1):
        yield i * (5 * i - 3) / 2

def generateSquareNumbers(numberLimit, startingNumber=1):
    ''' generator that produces square numbers for 1..numberLimit '''
    for i in xrange(startingNumber, numberLimit + 1):
        yield i ** 2

def phi(number, primeObject=ProjectEulerPrime()):
    ''' return totient(n). this is a naive implementation. look at problem 72 for an efficient way to do this 
    for multiple numbers you want phi() for.
     '''
    result = number
    for prime in frozenset(primeObject.factorize(number)): result *= 1 - float(1) / prime
    return int(result)