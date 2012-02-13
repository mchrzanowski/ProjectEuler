import scala.collection.mutable.HashMap

object Problem092 {

    val Limit = 10000000

    def main(args: Array[String]): Unit = {

        val start = System.currentTimeMillis
        
        val map = new HashMap[Int, Int]

        var solutions = 0
        
        for (i <- 1 until Limit){
            if(sumNumbers(i, i, map) == 89)
                solutions += 1
        }
        
        println("Number of numbers that sum to 89 <= " + Limit + " : " + solutions)
        
        val end = System.currentTimeMillis
        println("Runtime: " + (end - start) + " ms.")
    }

    def sumNumbers(i: Int, originalNumber: Int, map: HashMap[Int, Int]): Int = {
        
        val summation = i.toString.map(char => (char.toInt - '0') * (char.toInt - '0')).sum

        if (summation == 89 || summation == 1){
            map.put(originalNumber, summation)
            summation
        }

        else if (map.contains(summation)){
            map.getOrElse(summation, 0)
        }

        else 
            sumNumbers(summation, originalNumber, map)
    }

}