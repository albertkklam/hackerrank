# Sherlock and Moving Tiles
## https://www.hackerrank.com/challenges/sherlock-and-moving-tiles/problem

import math
L, S1, S2 = map(int, raw_input().strip().split(' '))
for _ in range(int(raw_input().strip())):
    s = abs(S1 - S2) / math.sqrt(2)
    print format((L - math.sqrt(int(raw_input().strip()))) / s, '.20f')
