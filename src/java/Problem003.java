package projectEuler;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Set;
import java.util.HashSet;

public class Problem003 {
	
	public static void main (String[] args){
		
		final long LIMIT = 600851475143L;
		
		Set<Long> factors = new HashSet<Long>();
		
		long stopNumber = LIMIT;
		long l = 2;		
		
		do {
			
			long otherFactor = LIMIT / l;
			
			if (!factors.contains(l) && 
					!factors.contains(otherFactor) &&
					LIMIT % l == 0 ){
				factors.add(l);
				factors.add(otherFactor);	
				
				if (otherFactor < stopNumber){
					stopNumber = otherFactor;
				}

			}
			
			l++;
			
		} while (l <= stopNumber);
		
		List<Long> primes = new ArrayList<Long>();
		
		for (long ll : factors){
			boolean isNotPrime = false;
			for (long li = 2; li < ll; li++){
				if (ll % li == 0){
					isNotPrime = true;
					break;
				}
			}
			if (!isNotPrime){
				primes.add(ll);
			}
		}
		
		Collections.sort(primes);
		
		for (long prime : primes){
			System.out.println(prime);
		}
		
	}

}
