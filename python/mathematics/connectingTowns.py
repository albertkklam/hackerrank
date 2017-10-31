# Connecting Towns
## https://www.hackerrank.com/challenges/connecting-towns/problem

from operator import mul
for _ in range(int(raw_input().strip())):
    towns = int(raw_input().strip())
    paths = map(int, raw_input().strip().split(' '))
    print reduce(mul, paths, 1) % 1234567  
