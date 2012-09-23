

import java.util.HashSet;
import java.util.Set;

public class Problem023 {

	final static int LIMIT = 28124;
	
	
	public static void main(String[] args) {

		byte[] array = new byte[LIMIT];
		
		Set<Integer> abundantNumbers = new HashSet<Integer>();
		
		for (int i = 1; i < LIMIT; i++){
			if (isNumberAbundant(i)){
				abundantNumbers.add(i);
			}
		}
		
		for (int i : abundantNumbers){
			for (int j : abundantNumbers){
				if (i + j < LIMIT){
					array[i + j] = 1;
				}
			}
		}
		
		int sum = 0;
		for (int i = 0; i < array.length; i++){
			if (array[i] == 0){
				sum += i;
			}
		}
		
		System.out.println(sum);
		
	}
	
	
	private static boolean isNumberAbundant(int number) {
		
		Set<Integer> divisors = getDivisors(number);
		int sum = 0;
		for (int i : divisors){
			sum += i;
		}
		
		if (number < sum){
			return true;
		}
		return false;
	}
	
	private static Set<Integer> getDivisors(int number) {
		Set<Integer> divisors = new HashSet<Integer>();
		
		for (int i = 2; i < number / 2; i++){
			if (number % i == 0){
				divisors.add(i);
				divisors.add(number / i);
			}
		}
		return divisors;
	}

}
