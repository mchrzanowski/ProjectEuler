'''
Created on Feb 4, 2012

@author: mchrzanowski
'''

import os.path
from time import time

cardNumberToArrayDict = {}
arrayToCardNumberDict = {}
suitToArrayDict = {}
arrayToSuitDict = {}
evaluationDict = {}

def doesContainRoyalFlush(hand):
    for suit in suitToArrayDict:
        if hand[cardNumberToArrayDict['T']][suitToArrayDict[suit]] == 1 and  \
        hand[cardNumberToArrayDict['J']][suitToArrayDict[suit]] == 1 and   \
        hand[cardNumberToArrayDict['Q']][suitToArrayDict[suit]] == 1 and   \
        hand[cardNumberToArrayDict['K']][suitToArrayDict[suit]] == 1 and   \
        hand[cardNumberToArrayDict['A']][suitToArrayDict[suit]] == 1:
            return True
    return False

def getHighestCardInHand(hand, ignoreSpecificCardNumbers = False):
    for i in xrange(len(arrayToCardNumberDict) - 1, -1, -1):
        for j in xrange(len(suitToArrayDict)):
            if hand[i][j] == 1:
                if ignoreSpecificCardNumbers is not False and arrayToCardNumberDict[i] in ignoreSpecificCardNumbers:
                    continue
                return arrayToCardNumberDict[i]

def doesContainTwoPairs(hand):
    ''' check for one pair and then check for another pair by specifically asking
    the function to ignore the first number. Return the answer as a sorted list
    or False. '''
    firstPair = doesContainOnePair(hand)
    
    if firstPair is not False:
        secondPair = doesContainOnePair(hand, False, firstPair)
    
        if secondPair is not False:
            pair = [firstPair, secondPair]
            pair.sort()
            pair.reverse()
            return pair
    
    return False

def doesContainStraightFlush(hand):
    
    return doesContainStraight(hand, True)
    
def doesContainStraight(hand, mustBeInSameSuit = False):
    
    currentNumberInHand = -1
    iterations = 0
    suit = -1
    
    for i in xrange(len(arrayToCardNumberDict)):
        for j in xrange(len(suitToArrayDict)):
            if hand[i][j] == 1:
                if iterations == 0:
                    currentNumberInHand = i
                    iterations = 1
                    suit = j
                elif currentNumberInHand + 1 == i:
                    if mustBeInSameSuit and suit != j:
                        return False
                    currentNumberInHand = i
                    iterations += 1
                else:
                    return False
    
    if iterations == 5:
        return True
    
    return False

def doesContainOnePair(hand, onlyTwo = False, ignoreSpecificCardNumber = False):
    ''' Several switches here:
    onlyTwo : when turned on, this will force the method to return a card value whose frequency is EXACTLY 2.
    ignoreSpecificCardNumber: when on, the method will completely ignore a given card number '''
    for i in xrange(len(arrayToCardNumberDict) - 1, -1, -1):
        if ignoreSpecificCardNumber is not False and arrayToCardNumberDict[i] in ignoreSpecificCardNumber:
            continue
        number = 0
        for j in xrange(len(suitToArrayDict)):
            if hand[i][j] == 1:
                number += 1
        if (not onlyTwo and number >= 2) or (onlyTwo and number == 2) :
            return arrayToCardNumberDict[i]
            
    return False

def doesContainThreeOfAKind(hand, onlyThree = False):
    for i in xrange(len(arrayToCardNumberDict) - 1, -1, -1):
        number = 0
        for j in xrange(len(suitToArrayDict)):
            if hand[i][j] == 1:
                number += 1
        if (not onlyThree and number >= 3) or (onlyThree and number == 3):
            return arrayToCardNumberDict[i]
    return False

def doesContainFlush(hand):
    for suit in suitToArrayDict:
         numberOfCardsInSuit = 0
         for number in xrange(len(cardNumberToArrayDict)):
             if hand[number][suitToArrayDict[suit]] == 1:
                 numberOfCardsInSuit += 1
         if numberOfCardsInSuit == 5:
            return True
    return False

def doesContainFourOfAKind(hand, onlyFour = False):
    for i in xrange(len(arrayToCardNumberDict) - 1, -1, -1):
        numberOfMatchingCards = 0
        for j in xrange(len(suitToArrayDict)):
            if hand[i][j] == 1:
                numberOfMatchingCards += 1
        if (not onlyFour and numberOfMatchingCards >= 4) or (onlyFour and numberOfMatchingCards == 4):
            return arrayToCardNumberDict[i]
    return False

def doesContainFullHouse(hand):
    ''' of 5 cards, if there is a three of a kind, then  there can be only one pair.
    therefore, as long as these two numbers are not identical, then we have a full house.
    we enforce this check by specifically invoking the doesContainThreeOfAKind and doesContainOnePair methods
    with a flag ignoring card frequencies greater than three and two. '''
    threeOfAKindNumber = doesContainThreeOfAKind(hand, True)
    onePairNumber = doesContainOnePair(hand, True)
    
    if threeOfAKindNumber is not False and onePairNumber is not False:
        return tuple([threeOfAKindNumber, onePairNumber])
    
    return False
    
def setUpNumberDicts():
    cardNumberToArrayDict['2'] = 0   ; arrayToCardNumberDict[0] = '2'
    cardNumberToArrayDict['3'] = 1   ; arrayToCardNumberDict[1] = '3'
    cardNumberToArrayDict['4'] = 2   ; arrayToCardNumberDict[2] = '4'
    cardNumberToArrayDict['5'] = 3   ; arrayToCardNumberDict[3] = '5'
    cardNumberToArrayDict['6'] = 4   ; arrayToCardNumberDict[4] = '6'
    cardNumberToArrayDict['7'] = 5   ; arrayToCardNumberDict[5] = '7'
    cardNumberToArrayDict['8'] = 6   ; arrayToCardNumberDict[6] = '8'
    cardNumberToArrayDict['9'] = 7   ; arrayToCardNumberDict[7] = '9'
    cardNumberToArrayDict['T'] = 8   ; arrayToCardNumberDict[8] = 'T'
    cardNumberToArrayDict['J'] = 9   ; arrayToCardNumberDict[9] = 'J'
    cardNumberToArrayDict['Q'] = 10  ; arrayToCardNumberDict[10] = 'Q'
    cardNumberToArrayDict['K'] = 11  ; arrayToCardNumberDict[11] = 'K'
    cardNumberToArrayDict['A'] = 12  ; arrayToCardNumberDict[12] = 'A'

def setUpSuitDicts():
    suitToArrayDict['H'] = 0   ; arrayToSuitDict[0] = 'H'
    suitToArrayDict['S'] = 1   ; arrayToSuitDict[1] = 'S'
    suitToArrayDict['C'] = 2   ; arrayToSuitDict[2] = 'C'
    suitToArrayDict['D'] = 3   ; arrayToSuitDict[3] = 'D'

def setUpEvaluationDict():
    evaluationDict[9] = doesContainRoyalFlush
    evaluationDict[8] = doesContainStraightFlush
    evaluationDict[7] = doesContainFourOfAKind
    evaluationDict[6] = doesContainFullHouse
    evaluationDict[5] = doesContainFlush
    evaluationDict[4] = doesContainStraight
    evaluationDict[3] = doesContainThreeOfAKind
    evaluationDict[2] = doesContainTwoPairs
    evaluationDict[1] = doesContainOnePair
    evaluationDict[0] = getHighestCardInHand

def evaluate(hand, resultDict):
    ''' evaluate the hand. store results in a dict.
    key -> weight of hand 
    value -> actual result from method calls. '''
    
    for i in xrange(len(evaluationDict)):
        answer = evaluationDict[i](hand)
        if answer is not False:
            resultDict[i] = answer

def checkHighValueToTieBreak(firstHand, secondHand, ignoreList):
    ''' method to be used for tie breaking when two hands 
    have the same rank and are composed of the same cards. 
    In this scenario, we check the highest-valued card not part of the hand
    until we find an unequal one. '''
    firstNumber = secondNumber = 0
    
    while firstNumber == secondNumber:
        firstNumber = getHighestCardInHand(firstHand, ignoreList)
        secondNumber = getHighestCardInHand(secondHand, ignoreList)
        ignoreList.append(firstNumber)
     
    if firstNumber > secondNumber:
        return True
        
def doesFirstHandWin(firstDict, secondDict, firstHand, secondHand):
    
    if max(firstDict) > max(secondDict):
        return True
    
    elif max(firstDict) == max(secondDict):
        
        maxNumber = max(firstDict)
                        
        # 2 is a special case as that's where you can have two pairs.
        # so for that one, just check which result is greater
        if maxNumber == 2:
            
            # is the first greater?
            if cardNumberToArrayDict[firstDict[maxNumber][1]] > cardNumberToArrayDict[secondDict[maxNumber][1]]:
                return True
            
            # now try the second.
            if firstDict[maxNumber][1] == secondDict[maxNumber][1] and \
            cardNumberToArrayDict[firstDict[maxNumber][0]] > cardNumberToArrayDict[secondDict[maxNumber][0]]:
                return True
            
            # finally, use the highest card in the hand as a tie breaker
            if firstDict[maxNumber] == secondDict[maxNumber]:
                ignoreList = list(firstDict[maxNumber])
                return checkHighValueToTieBreak(firstHand, secondHand, ignoreList)
                
        
        # else, for any other test, check the results. the 
        # result consisting of higher-valued cards wins.
        elif cardNumberToArrayDict[firstDict[maxNumber]] > \
        cardNumberToArrayDict[secondDict[maxNumber]]:
            return True
        
        # if the two give the same result, check for the highest valued
        # card in the hand.
        elif firstDict[maxNumber] == secondDict[maxNumber]:
            ignoreList = list(firstDict[maxNumber])
            return checkHighValueToTieBreak(firstHand, secondHand, ignoreList)
        
    return False
       
def main():
    
    start = time()
    
    solutions = 0
    
    setUpNumberDicts()
    setUpSuitDicts()
    setUpEvaluationDict()
    
    file = open(os.path.join(os.curdir,'./requiredFiles/Problem054PokerHands.txt'), 'r')
    for row in file:
        row = row.rstrip()
        cards = row.split()
                
        firstHand = [[0 for column in xrange(len(suitToArrayDict))] for row in xrange(len(cardNumberToArrayDict))]
        secondHand = [[0 for column in xrange(len(suitToArrayDict))] for row in xrange(len(cardNumberToArrayDict))]
        for i in xrange(len(cards)):
            
            cardNumber = cardNumberToArrayDict[cards[i][0]]
            cardSuit = suitToArrayDict[cards[i][1]]
            
            if i < len(cards) / 2:
                firstHand[cardNumber][cardSuit] = 1
            else:
               secondHand[cardNumber][cardSuit] = 1
               
        firstHandResulsDict = {}
        secondHandResultsDict = {}
        
        evaluate(firstHand, firstHandResulsDict)
        evaluate(secondHand, secondHandResultsDict)
        
        if doesFirstHandWin(firstHandResulsDict, secondHandResultsDict, firstHand, secondHand):
            solutions += 1
        
    
    print "Games in which Player 1 wins: ", solutions
    end = time()
    print "Runtime: ", end - start, " seconds."     

if __name__ == '__main__':
    main()