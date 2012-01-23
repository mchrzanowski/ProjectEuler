package ProjectEulerLibrary;

import java.util.HashMap;
import java.util.Map;

public class Problem002 {
	
	final static long VALUE_LIMIT = 4000000;
		
	final static Map<Integer, Long> store = new HashMap<Integer, Long>();

	
	
	public static void main(String[] args){
		
		store.put(0, 1L);
		store.put(1, 2L);
		
		fib(50);
		
		long result = 0;
		
		for (int iteration : store.keySet()){
			
			System.out.println(iteration + ":\t" + store.get(iteration));
			
			if (store.get(iteration) % 2 == 0 && store.get(iteration) < VALUE_LIMIT){
				result += store.get(iteration);
			}
		}
		
		System.out.println(result);
		
		
		
		
	}
	
	private static Long fib(int iteration){
		
		long firstValue;
		long secondValue;
		
		if (store.containsKey(iteration - 1)){
			secondValue = store.get(iteration - 1);
		}
		else {
			secondValue = fib(iteration - 1 );
		}
		
		if (store.containsKey(iteration - 2)){
			firstValue = store.get(iteration - 2);
		}
		else {
			firstValue = fib(iteration - 2);
		}
		
		Long result =  firstValue + secondValue;
		store.put(iteration, result);
		
		return result;
		
	}

}
