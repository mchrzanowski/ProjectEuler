package ProjectEulerLibrary;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Problem022 {

	final static Map<Character, Integer> map = new HashMap<Character, Integer>();
	
	static {
		
		for (char c = 'A'; c <= 'Z'; c++){
			map.put(c, c - 'A' + 1);
		}
		
	}
	
	public static void main(String[] args) {
		List<String> listOfNames = null;
		try {
			listOfNames = readInFileToList();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		Collections.sort(listOfNames);
		
		long total = 0;
		
		for (int i = 0; i < listOfNames.size(); i++){
			int sum = 0;
			for (char c : listOfNames.get(i).toCharArray()){
				sum += map.get(c);
			}
			sum *= i + 1;
			total += sum;
		}
			
		System.out.println(total);

	}
	
	private static List<String> readInFileToList() throws FileNotFoundException {
		List<String> list = new ArrayList<String>();
		
		Scanner sc = new Scanner(new File("/Users/polak/Documents/workspace/JavaPlay/Problem022-Names.txt"));
		sc.useDelimiter(",");
		
		while (sc.hasNext()){
			String s = sc.next();
			s = s.replaceAll("\"", "");
			list.add(s);
		}
		return list;
	}

}
