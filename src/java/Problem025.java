

import java.math.BigInteger;
import java.util.HashMap;
import java.util.Map;

public class Problem025 {

	final static Map<Integer, BigInteger> store = new HashMap<Integer, BigInteger>();


	public static void main(String[] args){
		
		store.put(1, BigInteger.ONE);
		store.put(2, BigInteger.ONE);
		
		fib(5000);
		
		int result = Integer.MAX_VALUE;
		
		for (int iteration : store.keySet()){
			if (store.get(iteration).toString().length() == 1000){
				if (iteration < result){
					result = iteration;
				}
			}
		}
		
		System.out.println(result + " : " + store.get(result));
		
	}
	
	private static BigInteger fib(int iteration){
		
		BigInteger firstValue;
		BigInteger secondValue;
		
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
		
		BigInteger result =  firstValue.add(secondValue);
		store.put(iteration, result);
		
		return result;
		
	}

}
