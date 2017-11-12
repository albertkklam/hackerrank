# Filling Jars
## https://www.hackerrank.com/challenges/filling-jars/problem

n, m = map(int, raw_input().strip().split(' '))
total = 0
for _ in range(m):
    a, b, k = map(int, raw_input().strip().split(' '))
    total += (b - a + 1) * k
print total / n
