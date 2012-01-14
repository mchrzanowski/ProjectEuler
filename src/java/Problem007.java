package projectEuler;

public class Problem007 {

	final static int LIMIT = 10000000;
	final static int PRIME_LIMIT = 10001;
	
	public static void main(String[] args){
		
		int[] array = new int[LIMIT];
		
		for (int i = 2; i < LIMIT; i++){
			
			if (array[i] == 1){
				continue;
			}
			
			int multiplier = i + i;
			
			while (multiplier < LIMIT){
				array[multiplier] = 1;
				multiplier += i;
			}
			
//			System.out.println(i);
			
		}
		
		int primeNumber = 0;
		for (int i = 2; i < LIMIT; i++){
			if (array[i] == 0){
				primeNumber++;
				if (primeNumber == PRIME_LIMIT){
					System.out.println(i);
					System.exit(0);
				}
			}
		}
		
	}
}
