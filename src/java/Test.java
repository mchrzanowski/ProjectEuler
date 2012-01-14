package projectEuler;

import java.util.Scanner;

public class Test {

	public static void main(String[] args){
		
		Scanner sc = new Scanner(System.in);
		System.out.print("enter number:");
		Integer x = sc.nextInt();
		
		System.out.println("Received: " + x);
				
		System.out.println("Now: " + x);
		
		if(x < 1000){
			System.out.println("< 1000");
		}
		else if (x == 1000){
			System.out.println("EQUALS 1000");
		}
		else {
			System.out.println("> 1000");
		}
		
		int i = -1;
		
		while (i < x){
			System.out.println(i);
			i = i + 1;
		}
		
		int power = 3;
		
		i = 1;
		
		while (power > 0){
			
		// 10 ^ 3 = 10 * 10 * 10	
			i = i * 10;
			power = power - 1;
		}
		
		System.out.println(i);
		
		Integer divisionExample = i / 100;
		
		System.out.println(divisionExample);
		
		long a = divisionExample * 2;
		System.out.println(a);
		
		System.out.println(Integer.MAX_VALUE);
		System.out.println(Long.MAX_VALUE);
		
		double integerDvision = 3.0 / 2.0 ;
		
		System.out.println(integerDvision);
		
		
		
		
		
		
		

	}
	
}
