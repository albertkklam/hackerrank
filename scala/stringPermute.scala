// String-o-Permute
// Kazama gave Shaun a string of even length, and asked him to swap the characters at the even positions with the next character. Indexing starts at 0

object Solution {
    def main(args: Array[String]) {
		def swapString(s: String): String = {
		    def swap(sList: List[Char]): List[Char] = sList match {
		    	case Nil => Nil
		    	case x :: Nil => List(x)
		    	case x :: y :: rest => y :: x :: swap(rest)
		    }
		    val sList = s.toList
		    swap(sList).mkString("")
		}
		val inputs = io.Source.stdin.getLines.drop(1).toList
		for (x <- inputs) {
			println(swapString(x))
		}
	}
}
