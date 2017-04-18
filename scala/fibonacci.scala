// Fibonacci Numbers
// Complete the Fibonacci function to return the Nth term. We start counting from Fibonacci(1) = 0. This might differ from some other notations that treats Fibonacci(0) = 0

def fibonacci(x:Int):Int = x match {
    case 1 => 0
    case 2 => 1
    case _ => fibonacci(x-1) + fibonacci(x-2)
}
