// String Reductions
// Given a string consisting of lowercase English characters, remove all of the characters that occurred previously in the string. 

object Solution {
  def main(args: Array[String]) {
    def stringReduce(s: String): String = {
      def reduceHelper(sList: List[Char]): List[Char] = sList match {
        case Nil => Nil
    		case head :: tail => head :: reduceHelper(tail filterNot(_ == head))
      }
      val sList = s.toList
      reduceHelper(sList).mkString("")
    }
    val inputs = io.Source.stdin.getLines
    for (x <- inputs) {
      println(stringReduce(x))
    }
  }
}
