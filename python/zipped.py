# Zipped!
## https://www.hackerrank.com/challenges/zipped/problem
### Python 3.6

N, X = map(int, input().split(' '))
marks = []

for _ in range(X):
    marks.append(map(float, input().split(' ')))

averageMarks = [sum(m) / X for m in zip(*marks)]
print(*averageMarks, sep='\n')
