# Computing the Correlation
## https://www.hackerrank.com/challenges/computing-the-correlation/problem

import math
n = int(input().strip())

maths = []
physics = []
chemistry = []

for _ in range(n):
    m, p, c = input().strip().split('\t')
    maths.append(m)
    physics.append(p)
    chemistry.append(c)

def corr(x,y):
    ex = sum(x) / len(x)
    ey = sum(y) / len(y)
    exx = sum([a * b for a, b in zip(x,x)]) / len(x)
    exy = sum([a * b for a, b in zip(x,y)]) / len(x)
    eyy = sum([a * b for a, b in zip(y,y)]) / len(y)

    return (exy - ex * ey) / (math.sqrt(exx - ex ** 2) * math.sqrt(eyy - ey ** 2))

print("{0:.2f}".format(corr(list(map(int, maths)), list(map(int, physics)))))
print("{0:.2f}".format(corr(list(map(int, physics)), list(map(int, chemistry)))))
print("{0:.2f}".format(corr(list(map(int, maths)), list(map(int, chemistry)))))
