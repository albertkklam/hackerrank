# Cutting Paper Squares
## https://www.hackerrank.com/challenges/p1-paper-cutting/problem

def solve(n, m):
    return (n - 1) + (m - 1) * n

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
result = solve(n, m)
print(result)
