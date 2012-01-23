package ProjectEulerLibrary;

import java.util.HashMap;
import java.util.Map;

public class Problem017 {

	final static Map<Character, Integer> map = new HashMap<Character, Integer>();
	final static Map<Character, Integer> secondMap = new HashMap<Character, Integer>();
	
	final static int LIMIT = 1000;
	
	static {
		map.put('1', 3);
		map.put('2', 3);
		map.put('3', 5);
		map.put('4', 4);
		map.put('5', 4);
		map.put('6', 3);
		map.put('7', 5);
		map.put('8', 5);
		map.put('9', 4);
		map.put('0', 4);
		
		secondMap.put('0', 0);
		secondMap.put('2', 6);
		secondMap.put('3', 6);
		secondMap.put('4', 5);
		secondMap.put('5', 5);
		secondMap.put('6', 5);
		secondMap.put('7', 7);
		secondMap.put('8', 6);
		secondMap.put('9', 6);
	}
	
	public static void main(String[] args) {
		
		long result = 0L;
		
		for (int i = 1; i <= LIMIT; i++){
			
			
			String number = String.valueOf(i);
			
			if (number.length() == 4){
				result += 3;		// ONE
				result += 8;		// THOUSAND
				continue;
			}
			
			if (number.length() == 3){
				
				result += map.get(number.charAt(0));
				result += 7;	// HUNDRED
				
				if (i % 100 != 0){
				
					result += 3;	// AND
					number = number.substring(1, 3);
					
				}
				else {
					continue;
				}
			}
			
			if (number.length() == 2){
				
				switch (Integer.parseInt(number)){
					case 10:	result += 3;
								number = "";
								break;
					case 11: 	result += 6;
								number = "";
								break;
					case 12:	result += 6;
								number = "";
								break;
					case 13:	result += 8;
								number = "";
								break;
					case 14:	result += 8;
								number = "";
								break;
					case 15:	result += 7;
								number = "";
								break;
					case 16: 	result += 7;
								number = "";
								break;
					case 17:	result += 9;
								number = "";
								break;
					case 18:	result += 8;
								number = "";
								break;
					case 19:	result += 8;
								number = "";
								break;
					case 20:	result += 6;
								number = "";
								break;
					case 30:	result += 6;
								number = "";
								break;
					case 40:	result += 5;
								number = "";
								break;
					case 50:	result += 5;
								number = "";
								break;
					case 60:	result += 5;
								number = "";
								break;
					case 70:	result += 7;
								number = "";
								break;
					case 80:	result += 6;
								number = "";
								break;
					case 90:	result += 6;
								number = "";
								break;
					default:	result += 0;
								break;
				}
								
				if (number.length() == 2){
					result += secondMap.get(number.charAt(0));
					number = String.valueOf(number.charAt(1));
				}
			}
			
			if (number.length() == 1){
				result += map.get(number.charAt(0));
			}
			
	//		System.out.println("i: " + i + " :\t" + result);
			
		}
		
		System.out.println(result);
		
	}

}
