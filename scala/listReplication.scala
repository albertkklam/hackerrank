// List Replication
// Given a list, repeat each element in the list n amount of times

def f(num:Int,arr:List[Int]): List[Int] = arr.flatMap(List.fill(num)(_))
