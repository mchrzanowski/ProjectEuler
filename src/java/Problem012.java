package ProjectEulerLibrary;

import java.util.HashSet;
import java.util.Set;

public class Problem012 {

	public static void main(String[] args) {
		
		final long start = System.currentTimeMillis();
		
		int currentSize = 1;
		
		final int DIVISOR_LIMIT = 500;
		
		Long result = 0L;
		
		while (currentSize < 1000000){
		
				result += currentSize;
												
				final int size = getDivisors(result);
				
				if (size >= DIVISOR_LIMIT){
					System.out.println("Row: " + currentSize + "\tSigma:\t" + result + "\tSize:\t" + size);
					break;
				}
					
			currentSize++;
			
		}
		
		final long end = System.currentTimeMillis();
		System.out.println("Time: " + (end - start) + " ms.");
	}
	
	private static int getDivisors(final long number) {
		final Set<Long> divisors = new HashSet<Long>();
						
		divisors.add(1L);
		divisors.add(number);
		
		final Double sqrt = Math.sqrt(number);
		final Long sqrtTruncation = sqrt.longValue();
		
		
		// perfect square check.
		if (sqrt.equals(sqrtTruncation.doubleValue())){
			divisors.add(sqrtTruncation);
		}
		
		// perfect square fail. continue onwards to the normal divisor scan check.
		else {
			for (long l = 2L; l <= sqrtTruncation; l++){
				if (number % l == 0){
					divisors.add(l);
					divisors.add(number / l);
				}
			}
		}
		return divisors.size();
	}

}
