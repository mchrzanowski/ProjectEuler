

public class Problem001 {

	public static void main (String[] args){
				
		int result = 0;
		
		final int TARGET = 1000;
		
		for (int i = 3; i < TARGET; i += 3){
			if (i %  5 != 0) {
				result += i;
			}
		}
		
		for (int i = 5; i < TARGET; i += 5){
			result += i;
		}
		
		System.out.println(result);
		
	}
	
}
