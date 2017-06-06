# Viral Advertising
## https://www.hackerrank.com/challenges/strange-advertising

n = int(raw_input().strip())
m = 5
count = 0
while n > 0:
    m /= 2
    count += m
    m *= 3 
    n -= 1
print count
