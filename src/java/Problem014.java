

import java.util.LinkedList;
import java.util.List;

public class Problem014 {
	
	final static int LIMIT = 1000000;
	
	
	public static void main(String[] args) {
		
		long begin = System.currentTimeMillis();
		
		int largestSequence = 1;
		Long largestStartingNumber = 1L;

		
		for (Long l = 1L; l < LIMIT; l++){
			List<Long> list = new LinkedList<Long>();
			list.add(l);
			generateSequence(list);
			if (list.size() > largestSequence){
				largestSequence = list.size();
				largestStartingNumber = l;
			}
		}
		
		System.out.println("Number: " + largestStartingNumber + "\t:\tSequence size: " + largestSequence);
		
		long end = System.currentTimeMillis();
		System.out.println("Took: " + (end - begin) + " ms.");
		
	}
	
	public static void generateSequence(List<Long> currentSequence){
						
		while (currentSequence.get(currentSequence.size() - 1) > 1){
			
			Long lastNumber = currentSequence.get(currentSequence.size() - 1);
			
			if (lastNumber % 2 == 0){
				currentSequence.add(lastNumber / 2);
			} 
			else {
				currentSequence.add(3 * lastNumber + 1);
			}
		}
		
	}

}
