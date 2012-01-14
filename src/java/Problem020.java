package projectEuler;

import java.math.BigInteger;

public class Problem020 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		final int LIMIT = 100;
		BigInteger factorialResult = BigInteger.ONE;
		for (Integer i = 1; i <= LIMIT; ++i){
			factorialResult = factorialResult.multiply(new BigInteger(i.toString()));
		}
		long result = 0;
		for (char c : factorialResult.toString().toCharArray()){
			result += c - '0';
		}
		System.out.println(result);
	}

}
