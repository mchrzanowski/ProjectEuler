'''
Created on Jan 19, 2012

@author: mchrzanowski
'''

from ProjectEulerPrime import ProjectEulerPrime


def pi(number):
    ''' naive implementation of the prime counting function'''
    return len(sieveOfEratosthenes(number))


def sieveOfEratosthenes(number, storedList=[]):
    ''' naive implementation of sieve algo '''
    from math import sqrt

    if len(storedList) < number:

        del storedList[:]

        storedList.extend([0 for number in xrange(number + 1)])

        storedList[0] = storedList[1] = 1

        for i in xrange(2, int(sqrt(number)) + 1):
            if storedList[i] == 1:
                continue
            currentValue = i ** 2
            while currentValue < len(storedList):
                storedList[currentValue] = 1
                currentValue += i

    return tuple(number for number in xrange(number + 1) if storedList[number] == 0)


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
    ''' return totient(n). this is a naive implementation.
    look at problem 72 for an efficient way to do this
    for multiple numbers you want phi() for.
     '''
    result = number
    for prime in frozenset(primeObject.factorize(number)):
        result *= 1 - float(1) / prime
    return int(result)


def eea(a, b):
    """
        Extended Euclidean Algorithm for GCD
        from:
        http://mail.python.org/pipermail/edu-sig/2001-August/001665.html
    """
    from operator import sub

    v1 = [a, 1, 0]
    v2 = [b, 0, 1]
    while v2[0] != 0:
        p = v1[0] // v2[0]
        v2, v1 = map(sub, v1, (p * vi for vi in v2)), v2
    return v1


def modular_inverse(m, k):
    """
        Return b such that b*m mod k = 1, or 0 if no solution
        from:
        http://mail.python.org/pipermail/edu-sig/2001-August/001665.html
    """
    v = eea(m, k)
    return (v[0] == 1) * (v[1] % k)


def crt(ms, az):
    """
        Chinese Remainder Theorem:
        ms = list of pairwise relatively prime integers
        az = remainders when x is divided by ms
        (ai is 'each in as', mi 'each in ms')

        The solution for x modulo M (M = product of ms) will be:
        x = a1*M1*y1 + a2*M2*y2 + ... + ar*Mr*yr (mod M),
        where Mi = M/mi and yi = (Mi)^-1 (mod mi) for 1 <= i <= r.

        from:
        http://mail.python.org/pipermail/edu-sig/2001-August/001665.html
    """
    from operator import add, mul

    M = reduce(mul, ms)  # multiply ms together
    Ms = tuple(M / mi for mi in ms)   # list of all M/mi
    ys = tuple(modular_inverse(Mi, mi) for Mi, mi in zip(Ms, ms))  # uses inverse,eea
    return reduce(add, tuple(ai * Mi * yi for ai, Mi, yi in zip(az, Ms, ys))) % M
