'''
Created on Apr 12, 2012

@author: mchrzanowski
'''

from random import shuffle, uniform
from time import time

def roll(sides):
    ''' return an integer of [0, sides - 1] + 1 '''
    return int(uniform(0, sides)) + 1

def getClosestRailRoad(currentPosition, gameSquareMap):
    
    if currentPosition == gameSquareMap['CH1']:
        return gameSquareMap['R2']
    
    elif currentPosition == gameSquareMap['CH2']:
        return gameSquareMap['R3']
    
    elif currentPosition == gameSquareMap['CH3']:
        return gameSquareMap['R1'] 
    
    else: 
        raise Exception("No RR Found for ", currentPosition) 
    
def getClosestUtility(currentPosition, gameSquareMap):
    
    if currentPosition == gameSquareMap['CH1']:
        return gameSquareMap['U1']
    
    elif currentPosition == gameSquareMap['CH2']:
        return gameSquareMap['U2']
    
    elif currentPosition == gameSquareMap['CH3']:
        return gameSquareMap['U1']
    
    else:
        raise Exception("No Utility Found for ", currentPosition) 


def getCHCard(currentPosition, gameSquareMap, numberOfGameSquares, valuesToCareAbout={}, cards=[]):
    
    if len(cards) == 0:
        for i in xrange(16): cards.append(i)
        shuffle(cards)
        valuesToCareAbout['GO'] = 1
        valuesToCareAbout['JAIL'] = 2
        valuesToCareAbout['C1'] = 3
        valuesToCareAbout['E3'] = 4 
        valuesToCareAbout['H2'] = 5 
        valuesToCareAbout['R1'] = 6 
        valuesToCareAbout['R2'] = 7 
        valuesToCareAbout['R3'] = 8 
        valuesToCareAbout['U'] =  9 
        valuesToCareAbout['BACK'] = 10
    
    nextCard = cards.pop()
    cards.insert(0, nextCard)       # place in back
    
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
        return getClosestRailRoad(currentPosition, gameSquareMap)
    elif nextCard ==  valuesToCareAbout['U']:
        return getClosestUtility(currentPosition, gameSquareMap)
    elif nextCard ==  valuesToCareAbout['BACK']:
        return (currentPosition - 3) % numberOfGameSquares
    else:
        return currentPosition

def getCCCard(currentPosition, gameSquareMap, valuesToCareAbout={}, cards=[]):
    
    if len(cards) == 0:
        for i in xrange(16): cards.append(i)
        shuffle(cards)
        valuesToCareAbout['GO'] = 12
        valuesToCareAbout['JAIL'] = 3
    
    nextCard = cards.pop()
    cards.insert(0, nextCard)       # place in back
    
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
    
    DIE_SIDES = 4
    GAME_SQUARES = 40
    
    ITERATIONS = 10 ** 7
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
        
        # Community Chance cards have a 10 / 16 chance of landing elsewhere.
        elif place in gameSquareMap['CH']:
            place = getCHCard(place, gameSquareMap, GAME_SQUARES)
        
        # evaluate this outside of the if / else block above
        # as there's a chance of landing on a CC square
        # from one of the CH squares.
        # CC Cards have a 2 / 16 chance of landing elsewhere.
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