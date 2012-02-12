
object Problem072 {
	
	val Limit = 1000

	def main(args: Array[String]): Unit = {
		val start = System.currentTimeMillis

		var runningTotal = 0
		for (denominator <- 2 to Limit) {
			var solutions = 0
			for (numerator <- 1 until denominator)
				if (gcd(numerator, denominator) == 1)
					solutions += 1

			println(denominator + " : " + solutions)
			runningTotal += solutions
		}
		
		println("Total: " + runningTotal)
		val end = System.currentTimeMillis

		println("Runtime: " + (end - start) +  " ms.")
	}


	def gcd(a: Int, b: Int): Int =
		if (b == 0) a else gcd(b, a % b)
}