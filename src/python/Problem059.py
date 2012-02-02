'''
Created on Feb 2, 2012

@author: mchrzanowski
'''
from csv import reader
import os.path
from time import time

def generateCommonWords():
    wordFile = open(os.path.join(os.curdir,'./requiredFiles/MostCommonEnglishWords.txt'), 'r')
        
    for word in wordFile: 
        yield word.rstrip('\n')
       
def generateCipheredSequence():
    cipherFile =  reader(open(os.path.join(os.curdir,'./requiredFiles/Problem059CipherText.txt'), 'r'), delimiter = ',')
    
    for row in cipherFile: 
        for number in row: 
            yield int(number)
            
def decryptUsingKey(text, keyTuple):
    i = 0
    while i < len(text):
        
        offset = 0
        for j in xrange(len(keyTuple)):
            if i + offset < len(text):
                yield int(text[i + offset]) ^ keyTuple[j]
                offset += 1
            else:
                break
        i += offset

def discoverLikelyKey(encryptedNumberList, commonWordSet):
    STARTING_LETTER = 'a'
    ENDING_LETTER = 'z'
    
    highestHitCount = None
    mostLikelyKey = None
    
    # iterate through potential ciphers.
    for a in xrange(ord(STARTING_LETTER), ord(ENDING_LETTER) + 1):
        for b in xrange(ord(STARTING_LETTER), ord(ENDING_LETTER) + 1):
            for c in xrange(ord(STARTING_LETTER), ord(ENDING_LETTER) + 1):
                
                candidateKey = tuple([a, b, c])
                decryptedString = ''.join([chr(letter).lower() for letter in decryptUsingKey(encryptedNumberList, candidateKey)]) 
                # one case for consistency.
                
                candidateHits = 0
                for word in commonWordSet:      
                    if word in decryptedString: # linear scans suck. but they're intuitive.
                        candidateHits += 1
                
                if candidateHits > highestHitCount:
                    highestHitCount = candidateHits
                    mostLikelyKey = candidateKey
    
    return mostLikelyKey
 
def main():
    ''' create a set containing the most common 100 English words (thanks, Wikipedia!).
    then run through all possible cipher possibilities. XOR the ciphered sequence against this candidate cipher.
    the candidate which produces the most matches to the set wins the tournament. '''
    
    start = time()
    
    commonWordSet = set([])
    for word in generateCommonWords():
        commonWordSet.add(word.rstrip('\n'))
    
    encryptedNumberList = [number for number in generateCipheredSequence()]
    
    key = discoverLikelyKey(encryptedNumberList, commonWordSet)
    sumOfDecryptedList = sum([letter for letter in decryptUsingKey(encryptedNumberList, key)])
    
    print "Suspected key: ", [chr(number) for number in key]
    print "Sum of ASCII in Decrypted Text: ", sumOfDecryptedList
    end = time()
    print "Runtime: ", end - start, " seconds."
    
if __name__ == '__main__':
    main()