package ProjectEulerLibrary;

import java.math.BigInteger;

public class Problem010 {

	final static int LIMIT = 2000000;
	
	public static void main(String[] args){
		
		int[] array = new int[LIMIT];
		
		for (int i = 2; i < LIMIT ; i++){
			
			if (array[i] == 1){
				continue;
			}
			
			int multiplier = i + i;
			
			while (multiplier < LIMIT){
				array[multiplier] = 1;
				multiplier += i;
			}
						
		}
		
		BigInteger primeNumberSum = BigInteger.ZERO;
		for (int i = 2; i < LIMIT; i++){
			if (array[i] == 0){
				primeNumberSum = primeNumberSum.add(new BigInteger(Integer.valueOf(i).toString()));	
			}
		}
		
		System.out.println(primeNumberSum);
	}

}
