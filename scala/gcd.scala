// Computing the GCD
// Given two integers x and y, a recursive technique to find their GCD is the Euclidean Algorithm

def gcd(x: Int, y: Int): Int = y match {
    case 0 => x;
    case _=> gcd(y, x%y)
}
