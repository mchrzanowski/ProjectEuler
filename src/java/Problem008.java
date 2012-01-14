package projectEuler;

public class Problem008 {

	final static String target = "73167176531330624919225119674426574742355349194934969835203127745" +
			"0632623957831801698480186947885184385861560789112949495459501737958331952853208805511125406987471585238630507156" +
			"932909632952274430435576689664895044524452316173185640309871112172238311362229893423380308135336276614282806444486" +
			"64523874930358907296290491560440772390713810515859307960866701724271218839987979087922749219016997208880937766572733300105" +
			"33678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290" +
			"8625693219784686224828397224137565705605749026140797296865241453510047482166370484403199890008895243450658541227588666" +
			"8811642717147992444292823086346567481391912316282458617866458359124566529476545682848912883142607690042242190226710556" +
			"2632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899" +
			"125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450";
	
	public static void main(String[] args) {
		
		int max = 0;
				
		for (int i = 0; i < target.length() - 4; ++i){
			int product = 1;
			int digitCounter = i;
			
			while (digitCounter <= i + 4){
				product *= target.charAt(digitCounter) - '0';
				digitCounter++;
			}
			if (product > max){
				max = product;
			}
		}
		
		System.out.println(max);
		
	}
}
