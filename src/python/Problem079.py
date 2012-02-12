'''
Created on Feb 12, 2012

@author: mchrzanowski
'''

import os.path
from time import time

def reconstuct_next_char_in_password(attempts, currentTarget, reconstructedPassword):
    
    newAttempt = currentTarget
    
    for attempt in attempts:
        if currentTarget in attempt:
            for number in xrange(attempt.index(currentTarget)):
                if attempt[number] not in reconstructedPassword:
                   return reconstuct_next_char_in_password(attempts, attempt[number], reconstructedPassword)
    
    reconstructedPassword.append(currentTarget)
 
def find_next_number_to_try(attempts, reconstructedPassword):
    for attempt in attempts:
        for number in attempt:
            if number not in reconstructedPassword:
                return attempts.index(attempt), attempts[attempts.index(attempt)].index(number)
    
def main():
    '''
    look for numbers that are only preceded by the numbers in the established list so far.
    else, check the new number.
    algo makes the implicit assumption that each number is present in the password only once
    as that's the most naive case.
    '''
    start = time()
    
    file = open(os.path.join(os.curdir,'./requiredFiles/Problem079KeyLog.txt'), 'r')
    attempts = [[char for char in attempt.rstrip("\n")] for attempt in file]
    
    allNumbers = set([])
    for attempt in attempts:
        for number in attempt:
            if number not in allNumbers:
                allNumbers.add(number)
    
    reconstructedPassword = []
    while len(reconstructedPassword) < len(allNumbers):
        matrixLocation = find_next_number_to_try(attempts, reconstructedPassword)
        reconstuct_next_char_in_password(attempts, attempts[matrixLocation[0]][matrixLocation[1]], reconstructedPassword)
    
    print "Reconstructed password: ", ''.join(reconstructedPassword)
    end = time()
    print "Runtime: ", end - start, " seconds."
    
if __name__ == '__main__':
    main()