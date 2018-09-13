# Maximize It!
## https://www.hackerrank.com/challenges/maximize-it/problem
### Python 2.7

import itertools
K, M = map(int, raw_input().strip(" ").split())

maximum = []
for k in xrange(K):
    maximum.append(map(lambda x:x**2,map(int,raw_input().strip(" ").split()[1:])))

print max(map(lambda x:x%M, map(sum, itertools.product(*maximum))))
