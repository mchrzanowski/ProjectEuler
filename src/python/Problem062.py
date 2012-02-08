'''
Created on Feb 7, 2012

@author: mchrzanowski
'''
from time import time

MATCHES = 5


def main():
    
    start = time()
    cubeDict = {}

    solution = 0
    candidate = 1
    while solution == 0:
                
        cube = str(candidate ** 3)
        
        keyList = [char for char in cube]
        keyList.sort()
        
        key = ''.join(keyList)
        
        cubeDict.setdefault(key, set([]))  
        cubeDict[key].add(cube)
        
        if len(cubeDict[key]) == MATCHES:
            solution = key
        
        candidate += 1
    
    print "Smallest 5-way string: ", min(cubeDict[key])
    end = time()
    print "Runtime: ", end - start, " seconds."
        
        

if __name__ == '__main__':
    main()