

public class Problem006 {

	public static void main(String[] args){
		final int LIMIT 	= 100;
		long sumOfSquares	= 0;
		long squareOfSum 	= 0;
		for (byte b = 1; b <= LIMIT; ++b){
			sumOfSquares 	+= b * b;
			squareOfSum 	+= b;
		}
		squareOfSum *= squareOfSum;
		long result = sumOfSquares - squareOfSum;
		System.out.println(result);
	}
}
