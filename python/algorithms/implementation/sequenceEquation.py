# Sequence Equation
## https://www.hackerrank.com/challenges/permutation-equation

n = int(raw_input().strip())
p = map(int, raw_input().strip().split(' '))
dic = {p[x-1]: x for x in range(1,n+1)}
for x in range(1,n+1):
    print dic[dic[x]]
