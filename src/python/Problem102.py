'''
Created on Mar 13, 2012

@author: mchrzanowski
'''

import os.path
from time import time

def loadTriangles(fileName):
    
    def getNumbersInPairs(points):
        counter = 0
        while counter + 1 < len(points):
            yield points[counter], points[counter + 1]
            counter += 2
    
    triangles = set([])
    for line in open(fileName):
        line = line.strip("\n\r")
        points = line.split(",")  
        triangle = []
        for x, y in getNumbersInPairs(points): triangle.append( (int(x), int(y)) )
        triangles.add(tuple(triangle))
        
    return triangles    

def isPointInsideTriangle(triangle, point):
    ''' 
    calculate the barycentric coordinates of the origin relative to the triangle vertices.
    if all three coordinates sum to > 1 or if any barycentric coordinate is < 0, then the point
    doesn't fall in the triangle area.
    http://www.blackpawn.com/texts/pointinpoly/default.html
    http://en.wikipedia.org/wiki/Barycentric_coordinates_%28mathematics%29
    '''
    # calculate vectors from the differences of the vertices and the point from a common source.
    v0 = (triangle[0][0] - triangle[1][0], triangle[0][1] - triangle[1][1])
    v1 = (triangle[2][0] - triangle[1][0], triangle[2][1] - triangle[1][1])
    v2 = (point[0] - triangle[1][0], point[1] - triangle[1][1])
    
    # take the dot products
    def dotProduct(u, v):
        if len(u) != len(v): raise Exception("the first vector's length (",len(u),") != second vector's length (",len(v),")")
        summation = 0
        for i in xrange(len(u)):
            summation += u[i] * v[i]
        return summation
    
    dot00 = dotProduct(v0, v0)
    dot01 = dotProduct(v0, v1)
    dot02 = dotProduct(v0, v2)
    dot11 = dotProduct(v1, v1)
    dot12 = dotProduct(v1, v2)
    
    # Compute barycentric coordinates
    invDenom = 1. / (dot00 * dot11 - dot01 * dot01)
    u = (dot11 * dot02 - dot01 * dot12) * invDenom
    v = (dot00 * dot12 - dot01 * dot02) * invDenom
    
    return u >= 0 and v >= 0 and u + v < 1

def main():
    
    ORIGIN = (0,0)
    solutions = 0
    triangles = loadTriangles(os.path.join(os.curdir, './requiredFiles/Problem102Triangles.txt'))
    for triangle in triangles:
        if isPointInsideTriangle(triangle, ORIGIN): solutions += 1
    
    print "Solutions:", solutions

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print "Runtime:", end - start, "seconds."
