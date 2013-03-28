from ProjectEulerPrime import ProjectEulerPrime
from ProjectEulerLibrary import phi

def main():

    # generate primes.
    p = ProjectEulerPrime()
    primes = {2}
    for i in xrange(3, 100000, 2):
        if p.isPrime(i):
            primes.add(i)

    ''' 
        We use the following facts:
            R(n) mod(n)
            => ((10 ** n - 1) / 9) mod n 
            => (10 ** n) mod (9 * n) = 1

            x ** y (mod n) == x ** (y mod phi(n)) (mod n)
        
        We stop once we detect a repeated residual
        (which means that we've entered a period).
        By sheer luck, I used a similar technique in problem 282
        to collapse much larger power towers.
    '''
    results = set()
    for prime in primes:
        phi_mod = phi(9 * prime)
        mod = 9 * prime
        seen_residuals = set()
        j = 1
        while True:
            residual = pow(10, pow(10, j, phi_mod), mod)
            if residual in seen_residuals:
                break
            if residual == 1:
                results.add(prime)
                break
            seen_residuals.add(residual)
            j += 1

    print "Sum: {}".format(sum(primes - results))

if __name__ == '__main__':
    import argparse
    import time

    start = time.time()

    parser = argparse.ArgumentParser(
        description="Problem 133. URL: http://projecteuler.net/problem=133")
    main()

    end = time.time()
    print "Runtime: {} seconds.".format(end - start)
