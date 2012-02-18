'''
Created on Jan 8, 2012

@author: mchrzanowski
'''

def main():
    min = -1000
    max = +1000
    
    maxA, maxB, maxPrimes = checkForPrimes(min, max)
    print "MaxA: ", maxA, "\nMaxB: ", maxB, "\nMaxPrimes: ", maxPrimes
    

def checkForPrimes(min, max):
    maxA = -1000
    maxB = -1000
    maxPrimes = []
    for a in range(min, max):
        for b in range(0, max): # b is in N as prime must be found when n = 0.
            primesFound = []
            for n in range(1, 1000):
                result = n ** 2 + a * n + b
                if isPrime(result):
                    primesFound.append(result)
                    if (len(primesFound) > len(maxPrimes)):
                        maxPrimes = primesFound
                        maxA = a
                        maxB = b
                else:
                    break
    return maxA, maxB, maxPrimes            
    
# from: http://www.daniweb.com/software-development/python/code/216880
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
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

if __name__ == '__main__':
    main()    
