import scala.io.Source
import scala.math
import java.io.File

object Problem082 {
    
    private val Size = 80
    private val file = new File(new File("./requiredFiles/").getCanonicalPath, "Problem082Matrix.txt")

    def main(args: Array[String]){
        
        val start = System.currentTimeMillis
        
        val problem =  new Problem082

        problem.readInFileToTransposedMatrix()
        
        val smallestSumAfterTraversal = problem.findSmallestSum()
        val end = System.currentTimeMillis
        
        println("Smallest sum: " + smallestSumAfterTraversal)
        println("Runtime: " + (end - start) + " milliseconds.")
    }

}

class Problem082 {

    val matrix = Array.ofDim[Int](Problem082.Size, Problem082.Size)

    def findSmallestSum(): Int = {
        
        // the first row can be completely skipped as we can start at any point there.
        // the last row is a special case as it just requires a downward summation.
        for (row <- 1 until matrix.length - 1){

            val downAndRightSums = Array.ofDim[Int](matrix.length)

            Array.copy(matrix(row), 0, downAndRightSums, 0, matrix(row).length)

            // first, a rightward and downward summation
            for (column <- 0 until matrix.length){
                if (column > 0)
                    downAndRightSums(column) += math.min(matrix(row - 1)(column), downAndRightSums(column - 1))
                else
                    downAndRightSums(column) += matrix(row - 1)(column)
            }
            
            // now, a leftward and downward summation. let downAndLeft store the minimum at each juncture.
            val downAndLeftSums = Array.ofDim[Int](Problem082.Size)
            
            Array.copy(matrix(row), 0, downAndLeftSums, 0, matrix(row).length)
            
            for (column <- matrix.length - 1 to 0 by -1){
                if (column < (matrix.length - 1))
                    downAndLeftSums(column) += math.min(matrix(row - 1)(column), downAndLeftSums(column + 1))
                else
                    downAndLeftSums(column) += matrix(row - 1)(column)
            }

            // now take the minimum between the two possibilities.
            for (column <- 0 until matrix.length)
                matrix(row)(column) = math.min(downAndRightSums(column), downAndLeftSums(column))
        }

        // sum downward as we never have to move horizontally on the last row.
        for (column <- 0 until matrix.length)
            matrix(Problem082.Size - 1)(column) += matrix(Problem082.Size - 2)(column)

        matrix(Problem082.Size - 1).min

    }

    /*
        We're going to read in the matrix in transposed so that we can work with 
        it in traditional (row, column) format. this alters the question from 
        allowing up, down, and right movement to allowing left, right, and down movement.
    */
    def readInFileToTransposedMatrix(): Unit = {
        val iterator = Source.fromFile(Problem082.file).getLines()

        for (row <- 0 until matrix.length){
            val newLine = iterator.next()
            val numbers = newLine.split(",")
            for (column <- 0 until matrix.length){
                matrix(column)(row) = numbers(column).toInt
            }
        }
    }

}

