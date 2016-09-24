# Maximize It!
## You are given a function f(x) = x ** 2. You are also given K lists. The i^th list consists of N_i elements
## You have to pick exactly one element from each list so that the equation below is maximized:
## S = (f(X_1) + f(X_2) + ... + f(X_K)) % M

import itertools
K, M = map(int, raw_input().strip(" ").split())

maximum = []
for k in xrange(K):
    maximum.append(map(lambda x:x**2,map(int,raw_input().strip(" ").split()[1:])))

print max(map(lambda x:x%M, map(sum, itertools.product(*maximum))))
