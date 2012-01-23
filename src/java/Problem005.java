package ProjectEulerLibrary;

public class Problem005 {
	
	final static int[] primes = {2, 3, 5, 7, 11, 13, 17, 19};
	
	final static int LIMIT = 20;
	
	public static void main(String[] args){
		int result = 1;
		
		
		for (byte b = 1; b <= LIMIT; ++b){
			while (result % b != 0){
				for (int prime : primes){
					if (b % prime == 0){
						result *= prime;
						break;
					}
				}
				
			}
		}
		
		System.out.println(result);
	}

}
