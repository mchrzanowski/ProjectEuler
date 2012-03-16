import scala.collection.mutable.HashMap

object Problem104 {

    def main(args: Array[String]): Unit = {

        val start = System.currentTimeMillis

        println(generateCorrectFibNumber())

        val end = System.currentTimeMillis

        println("Runtime: " + (end - start) + " ms.")
    }

    def generateCorrectFibNumber(): BigInt = {
        
        val memoizeMap = new HashMap[Long, BigInt]

        memoizeMap.put(0, 0)
        memoizeMap.put(1, 1) 

        val pandigitalSet = (1 until 10).toSet

        val areNumberEndsPandigital = (number: BigInt) => {

            String headNumber = 

            val head = (0 until pandigitalSet.size).map(number => ) * 
                math.pow(10, pandigitalSet.size).toInt).toInt.toString.toList.map(x => x - '0')

            println(head)
            println(
            (    (BigDecimal(number) / math.pow(10, pandigitalSet.size)) * 
                math.pow(10, pandigitalSet.size)    )  )
            
            val tail = (number % math.pow(10, pandigitalSet.size).toInt).toInt.toString.toList.map(x => x - '0')

            head.size >= pandigitalSet.size &&
            tail.size >= pandigitalSet.size &&
            head.slice(0, pandigitalSet.size).toSet.equals(pandigitalSet) 
//            &&
//            tail.slice(0, pandigitalSet.size).toSet.equals(pandigitalSet)
            
        }

        var currentNumber = 2
        var solution = 0

        while (solution == 0){
            generateFibNumber(memoizeMap, currentNumber)
            if (currentNumber == 2749){
                println("Trying for " + currentNumber + " " + memoizeMap(currentNumber))
            }
            if (areNumberEndsPandigital(memoizeMap(currentNumber))){
                solution = currentNumber
            }
            if (currentNumber == 2749){
                System.exit(0)
            }
            currentNumber += 1
        }

        currentNumber - 1       // subtract one based on how we're counting.
        
    }

    def generateFibNumber(map: HashMap[Long, BigInt], current: Long) = {

        val fibMinusOne = map(current - 1)
        val fibMinusTwo = map(current - 2)
        val result = fibMinusOne + fibMinusTwo
        
        map.put(current, result)
    }

}