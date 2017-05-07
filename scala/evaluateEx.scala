// Evaluating e^x
// Evaluate e^x for given values of x by using the expansion for the first 10 terms

object Solution { 
	def evalex(num: Double): Double = {
		def factorial(n: Int): Int = n match {
			case 0 => 1
			case _ => n * factorial(n-1)
		}
		List.range(0,10).map(x => scala.math.pow(num,x) / factorial(x)).sum
	}

	def main(args: Array[String]) {
	    val sc = new java.util.Scanner (System.in)
	    val n = sc.nextInt()
	    var a0 = 0
	    while(a0 < n) {
	        var x = sc.nextDouble()
	        println(evalex(x))
	        a0+=1;
	    }
	}
}
