# The Hurdle Race
## https://www.hackerrank.com/challenges/the-hurdle-race

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
height = map(int, raw_input().strip().split(' '))
print max(max(height) - k, 0)
