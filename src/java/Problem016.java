

import java.math.BigInteger;

public class Problem016 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {

		BigInteger bI = BigInteger.ONE;
		for (int i = 0; i < 1000; i++){
			bI = bI.multiply(new BigInteger("2"));
		}
		System.out.println(bI);
		int sum = 0;
		for (char c : bI.toString().toCharArray()){
			sum += c - '0';
		}
	
		System.out.println(sum);
	}

}
