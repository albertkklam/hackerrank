# Ice Cream Parlor
## https://www.hackerrank.com/challenges/icecream-parlor

t = int(raw_input().strip())
for _ in range(t):
    m = int(raw_input().strip())
    n = int(raw_input().strip())
    ar = map(int, raw_input().strip().split(' '))
    
    for i in range(n):
        if m - ar[i] in ar[i+1:]:
            print i+1, (ar[i+1:]).index(m-ar[i]) + (i+2)
            break
