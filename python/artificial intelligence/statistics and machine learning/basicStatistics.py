# Basic Statistics Warmup
## https://www.hackerrank.com/challenges/stat-warmup/problem

import numpy as np
from scipy import stats
n = int(input().strip())
num = list(map(int, input().strip().split(' ')))

print("{0:.1f}".format(np.mean(num)))
print("{0:.1f}".format(np.median(num)))
print(stats.mode(num)[0][0])
print("{0:.1f}".format(np.std(num)))
print("{0:.1f}".format(np.mean(num) - (1.96*np.std(num)) / np.sqrt(len(num))) + ' ' + "{0:.1f}".format(np.mean(num) + (1.96*np.std(num)) / np.sqrt(len(num))))
