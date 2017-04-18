// Sum of Odd Elements
// Return the sum of odd elements from the given list

def f(arr:List[Int]):Int = arr.filter(_ % 2 != 0).sum
