// Rotate String
// Your task is to display all n rotations of string s.

object Solution {
  def main(args: Array[String]) {
    def rotateString(s: String): List[String] = {
      def rotate(s: String, sList: List[String]): List[String] =  {
        val rotated = s.tail :+ s.head
        if(sList.length < s.length) rotate(rotated, sList :+ rotated)
        else sList
      }
        rotate(s, List())
    }
    val n = readInt()
    (0 until n).foreach(_ => println(rotateString(readLine().trim).mkString(" ")))
  }
}
