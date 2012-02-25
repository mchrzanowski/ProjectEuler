
object Problem078 {

    val ModValue = 1000000

    val ArraySize = 60000    // found through trial and error.

    def main(args:Array[String]) = {

        val start = System.currentTimeMillis

        val array = Array.ofDim[Int](ArraySize)

        array(0) = 1

        var solution = 0

        for (i <- 1 until ArraySize; if solution == 0){
            for (j <- i until ArraySize)
                array(j) = (array(j) + array(j - i)) % ModValue

            if (array(i) == 0)
                solution = i
        }

        println(solution)

        val end = System.currentTimeMillis
        println("Runtime: " + (end - start) + " ms.")

    }

}