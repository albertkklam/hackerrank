# Summing the N series
## https://www.hackerrank.com/challenges/summing-the-n-series/problem

for _ in range(int(raw_input().strip())):
    n = int(raw_input().strip())
    print n**2 % (10**9 + 7)
