# Extra Long Factorials
## https://www.hackerrank.com/challenges/extra-long-factorials

n = int(raw_input().strip())
i = 1

while n > 1:
    i *= n
    n -= 1

print i
