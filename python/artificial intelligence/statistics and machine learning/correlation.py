# Correlation and Regression Lines
## https://www.hackerrank.com/challenges/correlation-and-regression-lines-6/problem

import math

x = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

ex = sum(x) / len(x)
ey = sum(y) / len(y)
exx = sum([a * b for a, b in zip(x,x)]) / len(x)
exy = sum([a * b for a, b in zip(x,y)]) / len(x)
eyy = sum([a * b for a, b in zip(y,y)]) / len(y)

print((exy - ex * ey) / (math.sqrt(exx - ex ** 2) * math.sqrt(eyy - ey ** 2)))
