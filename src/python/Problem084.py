'''
Created on Apr 12, 2012

@author: mchrzanowski

* USE PYPY ONLY*
'''

from collections import deque
from random import shuffle, uniform
from time import time

def roll(sides):
    ''' return an integer of [0, sides - 1] + 1 '''
    return int(uniform(0, sides)) + 1

def getClosestNextLocation(currentPosition, locationsToGoTo, numberOfGameSquares):
    ''' 
    find the closest next point to go to based on the current position. 
    method will automatically loop to position zero once the end of the game board is reached 
    '''
    minMovement = numberOfGameSquares + 1
    travelPoint = None
    
    for location in locationsToGoTo:
        if location < currentPosition:  # we need to loop.
            movement = numberOfGameSquares - currentPosition + location
        else:
            movement = location - currentPosition
            
        if movement < minMovement:
            minMovement = movement
            travelPoint = location

    return travelPoint

def getCHCard(currentPosition, gameSquareMap, GAME_SQUARES, CH_CARDS=16, valuesToCareAbout={}, cards=deque()):
    ''' like the getCCCard method, but slightly more verbose owing to a greater number of important cards. '''
    if len(cards) == 0:
        for i in xrange(CH_CARDS): cards.append(i)
        shuffle(cards)
        if CH_CARDS < 10: raise Exception(CH_CARDS , "<", 10, ". Increase it!")
        valuesToCareAbout['GO'] = 0
        valuesToCareAbout['JAIL'] = 1
        valuesToCareAbout['C1'] = 2
        valuesToCareAbout['E3'] = 3 
        valuesToCareAbout['H2'] = 4 
        valuesToCareAbout['R1'] = 5 
        valuesToCareAbout['R2'] = 6 
        valuesToCareAbout['R3'] = 7 
        valuesToCareAbout['U'] =  8 
        valuesToCareAbout['BACK'] = 9
    
    nextCard = cards.popleft()
    cards.append(nextCard)       # place in back
    
    if nextCard == valuesToCareAbout['GO']:
        return gameSquareMap['GO']
    elif nextCard == valuesToCareAbout['JAIL']:
        return gameSquareMap['JAIL']
    elif nextCard ==  valuesToCareAbout['C1']:
        return gameSquareMap['C1']
    elif nextCard ==  valuesToCareAbout['E3']:
        return gameSquareMap['E3']
    elif nextCard ==  valuesToCareAbout['H2']:
        return gameSquareMap['H2']
    elif nextCard ==  valuesToCareAbout['R1']:
        return gameSquareMap['R1']
    elif nextCard == valuesToCareAbout['R2'] or nextCard == valuesToCareAbout['R3']:
        return getClosestNextLocation(currentPosition, gameSquareMap['R'], GAME_SQUARES)
    elif nextCard ==  valuesToCareAbout['U']:
        return getClosestNextLocation(currentPosition, gameSquareMap['U'], GAME_SQUARES)
    elif nextCard ==  valuesToCareAbout['BACK']:
        return (currentPosition - 3) % GAME_SQUARES
    else:
        return currentPosition

def getCCCard(currentPosition, gameSquareMap, CC_CARDS=16, valuesToCareAbout={}, cards=deque()):
    ''' 
        two CC cards matter of the (by default) 16 cards: advance to GO or to JAIL.
        create a randomized queue of cards, and then pop/push cards from the front to the back 
    '''
    if len(cards) == 0:
        for i in xrange(CC_CARDS): cards.append(i)
        shuffle(cards)
        if CC_CARDS < 2: raise Exception(CC_CARDS , "<", 2, ". Increase it!")
        valuesToCareAbout['GO'] = 0
        valuesToCareAbout['JAIL'] = 1
    
    nextCard = cards.popleft()
    cards.append(nextCard)       # place in back
    
    if nextCard == valuesToCareAbout['GO']:
        return gameSquareMap['GO']
    elif nextCard == valuesToCareAbout['JAIL']:
        return gameSquareMap['JAIL']
    else:
        return currentPosition
        
def getImportantGameSquareLocations():
    imporantSquares = {}
    
    imporantSquares['GO'] = 0
    imporantSquares['JAIL'] = 10
    imporantSquares['G2J'] = 30
    
    imporantSquares['CH1'] = 7
    imporantSquares['CH2'] = 22
    imporantSquares['CH3'] = 36
    imporantSquares['CH'] = set([imporantSquares['CH1'], imporantSquares['CH2'], imporantSquares['CH3']])
    
    imporantSquares['CC1'] = 2
    imporantSquares['CC2'] = 17
    imporantSquares['CC3'] = 33
    imporantSquares['CC'] = set([imporantSquares['CC1'], imporantSquares['CC2'], imporantSquares['CC3']])
    
    imporantSquares['C1'] = 11
    imporantSquares['E3'] = 24
    imporantSquares['H2'] = 39
    
    imporantSquares['R1'] = 5
    imporantSquares['R2'] = 15
    imporantSquares['R3'] = 25
    imporantSquares['R4'] = 35
    imporantSquares['R'] = set([imporantSquares['R1'], imporantSquares['R2'], imporantSquares['R3'], imporantSquares['R4']])
    
    imporantSquares['U1'] = 12
    imporantSquares['U2'] = 28
    imporantSquares['U'] = set([imporantSquares['U1'], imporantSquares['U2']])
    
    return imporantSquares

def main():
    
    # my first probabilistic problem in PE.
    # run through ITERATIONS different turns to determine 
    # the frequency of landing on a given square.
    
    DIE_SIDES = 4
    GAME_SQUARES = 40
    ITERATIONS = 10 ** 8
    ROLLS_TO_GO_TO_JAIL = 3
    
    gameSquareMap = getImportantGameSquareLocations()
    gameSquares = {}

    place = 0
    doubleRollCounter = 0
    
    for iteration in xrange(ITERATIONS):
        
        newRoll1 =  roll(DIE_SIDES)
        newRoll2 =  roll(DIE_SIDES)
        
        # check for 3 consecutive doubles
        if newRoll1 == newRoll2:
            doubleRollCounter += 1
        else:
            doubleRollCounter = 0 
        
        if doubleRollCounter == ROLLS_TO_GO_TO_JAIL:
            place = gameSquareMap['JAIL']
            doubleRollCounter = 0
        else:
            place = (place + newRoll1 + newRoll2) % GAME_SQUARES
        
        # check if we landed on G2J
        if place == gameSquareMap['G2J']:
            place = gameSquareMap['JAIL'] 
        
        # Chance cards have a chance of landing elsewhere.
        elif place in gameSquareMap['CH']:
            place = getCHCard(place, gameSquareMap, GAME_SQUARES)
        
        # evaluate this outside of the if / else block above
        # as there's a chance of landing on a CC square
        # from one of the CH squares.
        # Community Chest cards have a chance of landing elsewhere.
        if place in gameSquareMap['CC']:
            place = getCCCard(place, gameSquareMap)
                    
        if place not in gameSquares:
            gameSquares[place] = 1
        else:
            gameSquares[place] += 1
    
    
    print printMaxes(gameSquares, 3, ITERATIONS)
    

def printMaxes(gameSquares, number, ITERATIONS):
    
    dictCopy = gameSquares.copy()
    modalString = ''

    for i in xrange(number):
        
        maxKey = max(dictCopy, key=dictCopy.get)
#        print maxKey, dictCopy[maxKey], dictCopy[maxKey] / float(ITERATIONS)
        del dictCopy[maxKey]
        modalString += str(maxKey)
    
    return modalString    

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."