// Filter Positions in a List
// For a given list with N integers, return a new list removing the elements at odd positions

def f(arr: List[Int]): List[Int] = {
	arr.zipWithIndex.filter(_._2 % 2 == 1).map(_._1)
}
