# Best Divisor
## https://www.hackerrank.com/challenges/best-divisor/problem

n = int(raw_input().strip())
divisors = {i: sum(map(int, str(i))) for i in range(1, n+1) if n%i == 0}
max_value = max(divisors.values())
print min({key for key, value in divisors.items() if value == max_value})
