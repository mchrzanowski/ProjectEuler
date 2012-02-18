'''
Created on Feb 18, 2012

@author: mchrzanowski
'''

from time import time

TARGET = 2 * 10 ** 6
LIMIT = 10 ** 2     # the answer is bound to be pretty square-like as that provides more
                    # opportunities to form rectangles while adding very few additional blocks.
                    # and so we can avoid the extremes. 
                    # through numerical analysis, we see that it's very easy to hit 2 million;
                    # at row 100, we go past 2 million in first 35 rows. so a 100 * 100 grid is sufficient.
def main():
    
    start = time()
        
    winnerGridLocation = 0, 0
    
    matrix = [[0 for j in xrange(LIMIT + 1)] for i in xrange(LIMIT + 1)]
        
    for i in xrange(1, LIMIT + 1):
                        
        for j in xrange(1, LIMIT + 1):
            
            if matrix[j][i] != 0:
                
                matrix[i][j] = matrix[j][i]
            
            else:
                
                matrix[i][j] = matrix[i][j-1] + sum(range(j, i * j + 1, j))
                
                if abs(matrix[i][j] - TARGET) < abs(matrix[winnerGridLocation[0]][winnerGridLocation[1]] - TARGET):
                    
                    winnerGridLocation = i, j
                    
    
    print "Rectangle count closest to ", TARGET, " : ", matrix[winnerGridLocation[0]][winnerGridLocation[1]]
    print "Rectangle Size: ", winnerGridLocation[0] * winnerGridLocation[1]
    end = time()
    print "Runtime: ", end - start, " seconds."      

if __name__ == '__main__':
    main()