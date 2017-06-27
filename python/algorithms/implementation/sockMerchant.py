# Sock Merchant
## https://www.hackerrank.com/challenges/sock-merchant

n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
print sum([c.count(color) / 2 for color in set(c)])
