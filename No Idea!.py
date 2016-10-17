# No Idea!
## https://www.hackerrank.com/challenges/no-idea

n, m = map(int,raw_input().strip().split(' '))
arr = map(int,raw_input().strip().split(' '))

A = set(map(int, raw_input().strip().split(' ')))
B = set(map(int, raw_input().strip().split(' ')))

print sum([(i in A) - (i in B) for i in arr]) 
