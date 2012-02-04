import scala.io.Source
import scala.math
import java.io.File

object Problem081 {
	
	private val SIZE = 80
	private val file = new File(new File("./requiredFiles/").getCanonicalPath(), "Problem081Matrix.txt")

	def main(args: Array[String]){
		val start = System.currentTimeMillis();
		
		val problem =  new Problem081
		problem.readInFile()
		val smallestSumAfterTraversal = problem.findSmallestSum()
		val end = System.currentTimeMillis();
		
		println("Smallest sum: " + smallestSumAfterTraversal)
		println("Runtime: " + (end - start) + " milliseconds.")
	}

}

class Problem081 {

	private val matrix = Array.ofDim[Int](Problem081.SIZE, Problem081.SIZE)

	def findSmallestSum(): Int = {
		
		for (row <- 0 until matrix.length){
			for (column <- 0 until matrix.length){

				if (row > 0 && column > 0){
					matrix(row)(column) += math.min(matrix(row - 1)(column), matrix(row)(column - 1))
				}
				else if (row == 0 && column > 0){
					matrix(row)(column) +=  matrix(row)(column - 1)
				}
				else if (row != 0 && column == 0){
					matrix(row)(column) += matrix(row)(column) + matrix(row - 1)(column)
				}
			}
		}

		return matrix(Problem081.SIZE - 1)(Problem081.SIZE - 1)
	}


	def readInFile(): Unit = {
		val iterator = Source.fromFile(Problem081.file).getLines()

		for (row <- 0 until matrix.length){
			val newLine = iterator.next()
			val numbers = newLine.split(",")
			for (column <- 0 until matrix.length){
				matrix(row)(column) = numbers(column).toInt
			}
		}
	}

}