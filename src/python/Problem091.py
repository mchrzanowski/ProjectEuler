'''
Created on Mar 6, 2012

@author: mchrzanowski
'''

from time import time

LIMIT = 50

def main():
    
    # brute force out way through this
    solutions = 0
    
    usedPointCollection = set([])
    
    origin = (0, 0)
    
    # create first point from the origin.
    for xFirst in xrange(0, LIMIT + 1):
        for yFirst in xrange(0, LIMIT + 1):
            
            firstPoint = (xFirst, yFirst)
            
            if firstPoint == origin: continue
            
            # first leg distance. don't square to avoid errors.
            firstLeg = xFirst ** 2 + yFirst ** 2
            
            # firstPoints in this set can't be repeated by the (x,y)Second loops
            usedPointCollection.add(firstPoint)
                        
            for xSecond in xrange(0, LIMIT + 1):
                for ySecond in xrange(0, LIMIT + 1):
                    
                    secondPoint = (xSecond, ySecond)
                    
                    if secondPoint == origin: continue
                                        
                    if secondPoint in usedPointCollection: continue
                                                            
                    # second and third legs                
                    secondLeg = (xSecond - xFirst) ** 2 + (ySecond - yFirst) ** 2
                    
                    thirdLeg = xSecond ** 2 + ySecond ** 2  
                    
                    # right triangle means a ** 2 + b ** 2 == c ** 2
                    if firstLeg + secondLeg == thirdLeg     \
                    or thirdLeg + firstLeg == secondLeg     \
                    or thirdLeg + secondLeg == firstLeg:
                        solutions += 1
                        
                            
    print "Solutions: ", solutions

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."
    