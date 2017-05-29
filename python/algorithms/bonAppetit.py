# Bon Appetit
## https://www.hackerrank.com/challenges/bon-appetit

n, k = map(int, raw_input().strip().split(' '))
costs = map(int, raw_input().strip().split(' '))
b = int(raw_input())

if b - sum(costs[:k] + costs[k+1:]) / 2 != 0:
    print b - sum(costs[:k] + costs[k+1:]) / 2
else:
    print 'Bon Appetit'
