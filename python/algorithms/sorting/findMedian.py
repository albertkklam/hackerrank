# Find the Median
## https://www.hackerrank.com/challenges/find-the-median

n = int(raw_input().strip())
ar = sorted(map(int, raw_input().strip().split(' ')))
print ar[n/2]
