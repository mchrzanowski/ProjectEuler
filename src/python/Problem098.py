'''
Created on May 18, 2012

@author: mchrzanowski
'''

from itertools import permutations
from math import log10, sqrt
import os.path
from time import time

def get_anagrams(filename):
    
    anagrams = dict()
    
    with open(filename, 'r') as f:
        
        # first, sort the words into sets.
        for line in f:
            line = line.rstrip("\n\r")
            for word in line.split(","):
                word = word.strip("\"")
                
                key = ''.join(char for char in sorted(word))
                if key not in anagrams:
                    anagrams[key] = set()
                
                anagrams[key].add(word)
                
    # now, get rid of those sets with a cardinality of one
    for key, value in anagrams.items():
        if len(value) == 1:
            del anagrams[key]
    
    return anagrams

def map_number(anagram, letter_to_number_mapping):
    ''' at best a 1:1 mapping for each letter to a corresponding digit. it's at best
    because the first letter might get mapped to a zero '''
    result = 0
    power = len(anagram) - 1
    for letter in anagram:
        result += letter_to_number_mapping[letter] * 10 ** power
        power -= 1
    
    return result

def main():
    
    digits_sans_zero = frozenset(digit for digit in xrange(1, 9  + 1))
    anagrams = get_anagrams(os.path.join(os.curdir, './requiredFiles/Problem098Words.txt'))
    
    max_square = 0
        
    for key in anagrams:
        
        unique_chars = tuple(char for char in key)
        
        for start in digits_sans_zero:  # by definition, the first letter can't be mapped to 0. so, remove these possibilities.
            
            letter_mapping = dict()
            
            # brute force through all permutations.
            for other_mappings in permutations((digit for digit in xrange(0, 9 + 1) if digit != start), len(unique_chars) - 1):
                
                for i, letter in enumerate(unique_chars):
                    if i == 0:
                        letter_mapping[letter] = start
                    else:
                        letter_mapping[letter] = other_mappings[i - 1]
                
                mapping_produces_all_squares_flag = True
                max_square_this_round = 0
                
                for anagram in anagrams[key]:
                    
                    number = map_number(anagram, letter_mapping)
                    
                    # first part means that the first letter in the anagram transformed into a zero
                    # second part deals with finding perfect squares only.
                    if int(log10(number)) != len(anagram) - 1 or not sqrt(number).is_integer():
                        mapping_produces_all_squares_flag = False
                        break
                    
                    elif number > max_square_this_round:
                        max_square_this_round = number
                        
                if mapping_produces_all_squares_flag and max_square_this_round > max_square:
                    max_square = max_square_this_round
        
    print "Max square:", max_square

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."
