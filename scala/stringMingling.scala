// String Mingling
// You are given two strings P and Q, determine the mingled string R

object Solution {
    def main(args: Array[String]) {
        val p = readLine().toList
        val q = readLine().toList
        def f(p: List[Char], q: List[Char]): List[Char] = p match {
            case Nil => Nil
            case _ => p.head :: q.head :: f(p.tail, q.tail)
        }
        println(f(p, q).mkString(""))
    }
}
