# Most Distant
## https://www.hackerrank.com/challenges/most-distant/problem

import math

x = []
y = []

for _ in range(int(raw_input().strip())):
    xx, yy = map(int, raw_input().strip().split(' '))
    
    if xx == 0:
        y.append(yy)
    else:       
        x.append(xx)

xd = max(x) - min(x)
yd = max(y) - min(y)
xyd = math.sqrt(max(map(abs, x))**2 + max(map(abs, y))**2)
print ("%.6f" %max(xd, yd, xyd))
