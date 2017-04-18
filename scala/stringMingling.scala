// String Mingling
// You are given two strings P and Q, determine the mingled string R

val p = readLine().toList
val q = readLine().toList
    
def f(p: List[Char], q: List[Char]): List[Char] = {
    if (p.isEmpty) List()
    else (p.head :: q.head :: f(p.tail, q.tail))

}

println(f(p, q).mkString(""))
