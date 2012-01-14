package projectEuler;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Problem024 {
	
	 static int iterations = 725761;
	 static BigInteger result = new BigInteger("2013456789");
	 
	 final static int LIMIT = 1000000;
	 final static int NUMBERS = 10;
	 
	 final static Set<BigInteger> permutes = new HashSet<BigInteger>();
	 
	 final static Set<Character> charsToUse = new HashSet<Character>();

	 
	 static {
		 for (char c = '0'; c <= '9'; c++){
			 charsToUse.add(c);
		 }
		 permutes.add(result);
	 }

	
	public static void main(String[] args){
		
		
		String resultStr = result.toString();
		
		for (int i = resultStr.length() - 1; i >= 0; --i){
			String newString = resultStr.substring(0, i);
			permute(newString);
		}
				
	}
	
	private static void permute(String s){
		
		Set<Character> tSet = new HashSet<Character>(charsToUse);
		
		// remove numbers from set that we can't use.
		for (char c : s.toCharArray()){
			tSet.remove(c);
		}
				
		int combinations = 1;
		for (int i = 1; i <= tSet.size(); ++i) {
			combinations *= i;
		}
		
		Set<BigInteger> tNumbers = new HashSet<BigInteger>();
		
		// create all permutations.
		while (tNumbers.size() != combinations){
			
			List<Character> li = new ArrayList<Character>(tSet);
			String newS = s;
			while (!li.isEmpty()){
				
				int pick = Math.abs((int)(Math.random() * li.size()));
								
//				System.out.println("Pick: " + pick);
				newS += li.get(pick);
				li.remove(pick);
			}

			BigInteger potential = new BigInteger(newS);
			
			
			if (!tNumbers.contains(potential)){
				tNumbers.add(potential);
			}
		}
		
		// create list and sort.
		List<BigInteger> tList = new ArrayList<BigInteger>(tNumbers);
		Collections.sort(tList);
		
		// increment iterations.
		// store in permanent set.
		// have result == l
		for (BigInteger l : tList){
			
			if (permutes.contains(l)){
				continue;
			}
			
			if (l.toString().length() != NUMBERS){
				continue;
			}
			
			iterations++;
			permutes.add(l);
			result = l;
//			System.out.println("Iteration: " + iterations + " Result: \t" + result);
			
			if (iterations == LIMIT){
				System.out.println(result);
				System.exit(0);
			}
		}
	}

}

