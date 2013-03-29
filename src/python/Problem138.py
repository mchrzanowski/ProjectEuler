def main():
    
    '''
    God, I hate these recurrence relation problems.
    We are given the first two Ls: 17, 305.

    Note that:
        305 = 17 * 17 + 16 * 1
        5473 = 17 * 305 + 16 * 18
        ....
    Let P = [1, 18]. Then, the general formula, found with much
    trial and error, is:
        L_new = 17 * L[-1] + 16 * P[-1]
        P_new = L[-2] + L[-1] + P[-2] 
    '''

    Ls = [17, 305]
    remainders = [1, 18]

    for _ in xrange(10):
        quotient = 17 * Ls[-1]
        remainder = Ls[-2] + Ls[-1] + remainders[-2]
        Ls.append(quotient + 16 * remainders[-1])
        remainders.append(remainder)
        
    print "Solution: {}".format(sum(Ls))

if __name__ == '__main__':
    import argparse
    import time

    start = time.time()

    parser = argparse.ArgumentParser(description="Problem 138. URL: http://projecteuler.net/problem=138")
    main()

    end = time.time()
    print "Runtime: {} seconds.".format(end - start)