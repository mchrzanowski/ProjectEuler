package ProjectEulerLibrary;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Set;

public class Problem041 {

	 static BigInteger result = BigInteger.ZERO;
	 	 
	 final static Set<BigInteger> permutes = new HashSet<BigInteger>();
	 
	 
	 final public static int LIMIT = 10000000;

	 
	 final static Set<BigInteger> primeSet = getPrimes();
	
	public static void main(String[] args){
		
		for (int i = 1; i <= 9; i++){
			permute(Integer.valueOf(i).toString());
		}
				
	}
	
	private static void permute(String s){
		
		final Set<Character> charsToUse = new HashSet<Character>();

//		System.out.println(s);
		for (int i = 0; i <= 9; i++){
			
			if (Integer.parseInt(s) > i){
				continue;
			}
			charsToUse.clear();
//			System.out.println("Number: " + i);
			 for (char c = '1'; c <= i + '0'; c++){
				 charsToUse.add(c);
//				 System.out.print(Character.valueOf(c).toString() + ' ');
			 }
//			 System.out.println();
						
			// remove numbers from set that we can't use.
			for (char c : s.toCharArray()){
				charsToUse.remove(c);
			}
			
			Set<BigInteger> tNumbers = new HashSet<BigInteger>();
			
			getAllStringCombinations(s, tNumbers, i, charsToUse);
			
			for (BigInteger l : tNumbers){					
				if (l.compareTo(result) == 1){
					result = l;
					System.out.println(l);

				}				
			}
			

		}
		
	}
	
	private static void getAllStringCombinations(String s, Set<BigInteger> possibilities, int sizeLimit, Set<Character> characterSet){
		
		if (s.length() == sizeLimit && primeSet.contains(new BigInteger(s))){
			possibilities.add(new BigInteger(s));
		}
		else {
			for (char c : characterSet){
				String newS = s + c;
				Set<Character> remainingSet = new HashSet<Character>(characterSet);
				remainingSet.remove(c); // remove current character.
				getAllStringCombinations(newS, possibilities, sizeLimit, remainingSet);
			}
		}
	}
	
	private static Set<BigInteger> getPrimes(){
		
		Set<BigInteger> primeSet = new HashSet<BigInteger>();
		
		Double sqrt = Math.sqrt(LIMIT);
		Long truncatedSqrt = sqrt.longValue();
		
		int[] array = new int[LIMIT];
		
		for (int i = 2; i <= truncatedSqrt; i++){
			
			if (array[i] == 1){
				continue;
			}
			
			int multiplier = i + i;
			
			while (multiplier < LIMIT){
				array[multiplier] = 1;
				multiplier += i;
			}
						
		}
		
		for (int i = 2; i < LIMIT; i++){
			if (array[i] == 0){
				primeSet.add(new BigInteger(Integer.valueOf(i).toString()));
			}
		}
		return primeSet;
	}

}
