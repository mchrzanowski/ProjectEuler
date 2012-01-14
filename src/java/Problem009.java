package projectEuler;

public class Problem009 {

	final public static int LIMIT = 1000;
	
	static int first = 3;
	
	public static void main(String[] args) {
		
		while (true){
			int firstSquared 	= first * first;
			
			int second = first + 1;
			
			int result = 1;
			
			while (second < 1000){
				
				second++;
				
				int secondSquared 	= second * second;
				
				result				= firstSquared + secondSquared;
				
				double root			= Math.sqrt(result);
				
				if (root == ((int)Math.floor(root))){
					if (first + second + (int)root == LIMIT){
						System.out.println("first: " + first + "\tsecond: " + second + "\tresult: " + (int)root + "\tproduct: " + first * second * (int)root);
						System.exit(0);
					}
				}
			}
			first++;
		}
		
	}

}
