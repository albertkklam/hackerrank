# Closest Number
## https://www.hackerrank.com/challenges/closest-number/problem

for _ in range(int(raw_input().strip())):
    a, b, x = map(int, raw_input().strip().split(' '))
    c = a**b
    r = c%x
    c1 = int(c - r)
    c2 = int(c - r + x)
    if abs(c1 - c) <= abs(c2 - c):
        print c1
    else:
        print c2
