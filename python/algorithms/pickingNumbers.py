# Picking Numbers
## https://www.hackerrank.com/challenges/picking-numbers

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
print max([a.count(num) + a.count(num+1) for num in a])
