'''
Created on Jan 12, 2012

@author: mchrzanowski
'''

import os.path
from time import time

LIMIT = 100000  # to get this high, we'd need a word with an equivalent sum of 'Z' (26) 3800+ times

def createWordSet():
    
    wordFile =  open(os.path.join(os.curdir,'./requiredFiles/Problem042Words.txt'), 'r')
    wordSet = set([])
    for line in wordFile:
        wordList = line.split(",")
        for word in wordList:
            word = word.strip("\"")
            wordSet.add(word)
    wordFile.close()        
    return wordSet
            
def createTriangleSet():
    triangleSet = set([])
    for i in range(1, LIMIT + 1):
        triangleSet.add(int(0.5 * i * (i + 1)))
    return triangleSet
        

def main():
    begin = time()
    wordSet = createWordSet()
    triangleNumberSet = createTriangleSet()
    
    triangleWords = set([])
    
    for word in wordSet:
        resultingSum = 0
        for char in word:
            resultingSum = resultingSum + ord(char) - ord('A') + 1
        if resultingSum in triangleNumberSet:
            triangleWords.add(word)
            
    end = time()
    
    print "Words: ", triangleWords
    print "Number of Words: ", len(triangleWords)   
    print "Runtime: ", (end - begin), " seconds."  



if __name__ == '__main__':
    main()
