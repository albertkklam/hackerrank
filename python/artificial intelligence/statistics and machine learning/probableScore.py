# Correlation and Regression Lines - A Quick Recap #3
## https://www.hackerrank.com/challenges/correlation-and-regression-lines-8/problem

import numpy as np

x = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

m,b = np.polyfit(x, y, 1)
print(m*10 + b)
