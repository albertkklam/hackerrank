# Identify Smith Numbers
## https://www.hackerrank.com/challenges/identify-smith-numbers/problem

import math

def primeFactors(n):
    primes = []
    while n % 2 == 0:
        primes.append(2)
        n = n / 2
         
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            primes.append(i)
            n = n / i

    if n > 2:
        primes.append(n)
        
    return primes

n = int(raw_input().strip())

if sum(map(int, str(n))) == sum([sum(map(int, i)) for i in map(str, primeFactors(n))]):
    print 1
else:
    print 0
