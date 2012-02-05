'''
Created on Feb 5, 2012

@author: mchrzanowski
'''

from ProjectEulerPrime import ProjectEulerPrime
from time import time

def find5WayPrimes(primeList, primeObject):
        
    for a in xrange(len(primeList) - 4):
        
        first = str(primeList[a])
        
        for b in xrange(a + 1, len(primeList) - 3):
            
            second = str(primeList[b])
            
            if primeObject.isPrime(first + second) and primeObject.isPrime(second + first):
                
                for c in xrange(b + 1, len(primeList) - 2):
                    
                    third = str(primeList[c])
                    
                    if primeObject.isPrime(first + third) and primeObject.isPrime(third + first) \
                    and primeObject.isPrime(third + second) and primeObject.isPrime(second + third):
                    
                        for d in xrange(c + 1, len(primeList) - 1):
                            
                            fourth = str(primeList[d])
                            
                            if primeObject.isPrime(first + fourth) and primeObject.isPrime(fourth + first)    \
                            and primeObject.isPrime(fourth + second) and primeObject.isPrime(second + fourth)   \
                            and primeObject.isPrime(fourth + third) and primeObject.isPrime(third + fourth):
                                                     
                                for e in xrange(d + 1, len(primeList)):
                                    
                                    fifth = str(primeList[e])
                                    
                                    if primeObject.isPrime(fifth + first) and primeObject.isPrime(first + fifth)    \
                                    and primeObject.isPrime(fifth + second) and primeObject.isPrime(second + fifth)   \
                                    and primeObject.isPrime(fifth + third) and primeObject.isPrime(third + fifth)   \
                                    and primeObject.isPrime(fifth + fourth) and primeObject.isPrime(fourth + fifth):
                                           
                                        return [int(first), int(second), int(third), int(fourth), int(fifth)] 
    return None

def main():
    
    start = time()
    primeObject = ProjectEulerPrime()
    
    LIMIT = 10000   # setting a limit too high enables finding 5-way pairs that have huge last numbers (eg, 20000)
                    # 10,000 found through trial and error to be sufficient.
    

    primeList = [x for x in xrange(LIMIT) if primeObject.isPrime(x)]
    solutionList = find5WayPrimes(primeList, primeObject)
    
    print "Solutions: ", solutionList
    print "Sum: ", sum(solutionList)
    
    end = time()
    print "Runtime: ", end - start, " seconds."                                        

if __name__ == '__main__':
    main()