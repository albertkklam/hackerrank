# Reverse a List
## You are given a list of N elements. Reverse the list without using the reverse function

def reverse[A](l: List[A]): List[A] = l match {
    case head :: tail => reverse(tail) ::: List(head)
    case Nil => Nil
}
