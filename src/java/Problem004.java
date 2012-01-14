package projectEuler;

import java.util.Stack;

public class Problem004 {
		
	static int maxValue = 0;
	
	public static void main (String[] args){
		
		
		for (Integer j = 100; j < 1000; ++j){
									
			for (int i = 100; i < 1000; ++i){
				
				int result = j * i;
				
				Integer firstHalf 	= result / 1000;
				Integer secondHalf 	= result % 1000;
				
				String firstHalfStr 	= firstHalf.toString();
				String secondHalfStr 	= secondHalf.toString();
				
				firstHalfStr 	= addEnoughZeroes(firstHalfStr);								
				secondHalfStr 	= reverseString(addEnoughZeroes(secondHalfStr));
				
				if (firstHalfStr.equals(secondHalfStr)){
					if (result > maxValue){
						maxValue = result;
					}
				}
			}
		}
		
		System.out.println(maxValue);
		
	}
	
	private static String addEnoughZeroes(String s){
		while (s.length() < 3){
			s = '0' + s;
		}
		return s;
	}
	
	private static String reverseString(String s){
		Stack<Integer> stack = new Stack<Integer>();
		
		for (Character c : s.toCharArray()){
			stack.push(c - '0');
		}
		
		StringBuilder newNumber = new StringBuilder();
		while (!stack.empty()){
			newNumber.append(stack.pop().toString());
		}
		
		return newNumber.toString();
	}

}
