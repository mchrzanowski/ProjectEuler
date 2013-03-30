

public class Problem001 {

	public static void main (String[] args){
		
		int result = 0;
		
		final int TARGET = 1000;
		
		// arithmetic series for 3, 5, 15.
		int multiplesOfThree = (TARGET - 1) / 3;
		result += 3 * multiplesOfThree * (1 + multiplesOfThree) * 0.5;

		int multiplesOfFive = (TARGET - 1) / 5;
		result += 5 * multiplesOfFive * (1 + multiplesOfFive) * 0.5;

		int multiplesOfFifteen = (TARGET - 1) / 15;
		result -= 15 * multiplesOfFifteen * (1 + multiplesOfFifteen) * 0.5;

		System.out.println("Result: " + result);
		
	}
	
}
