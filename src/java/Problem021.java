package ProjectEulerLibrary;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Problem021 {

	final private static int LIMIT = 10000;
	
	final private static Set<Integer> amicableNumbers = new HashSet<Integer>();
			
	
	
	public static void main(String[] args) {

		
		for (int i = 0; i < LIMIT; i++){
			int sumOne = getSumOfDivisors(i);
			int sumTwo = getSumOfDivisors(sumOne);
			
			if (sumTwo == i && sumTwo != sumOne){
				amicableNumbers.add(sumTwo);
				amicableNumbers.add(sumOne);
			}
		}
		
		int sum = 0;
		for (int i : amicableNumbers){
			sum += i;
		}
		
		System.out.println(sum);

	}
	
	final private static Map<Integer, Integer> map = new HashMap<Integer, Integer>();
	
	private static int getSumOfDivisors(int number){
		
		if (map.containsKey(number)){
			return map.get(number);
		}
		
		int sum = 0;
		
		for (int i : getDivisors(number)){
			sum += i;
		}
		return sum;
	}
	
	private static Set<Integer> getDivisors(int number) {
		
		Set<Integer> divisors = new HashSet<Integer>();
		
		divisors.add(1); // by default.
		
		for (int i = 2; i < number / 2; i++) {
			if (number % i == 0) {
				divisors.add(i);
				divisors.add(number / i);
			}
		}
		return divisors;
	}

}
