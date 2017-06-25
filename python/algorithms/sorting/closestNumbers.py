# Closest Numbers
## https://www.hackerrank.com/challenges/closest-numbers

n = int(raw_input().strip())
ar = sorted(map(int,raw_input().strip().split(' ')))

diff = max(ar)
num = []
for i in range(n-1):
    if ar[i+1] - ar[i] < diff:
        num = [ar[i], ar[i+1]]
        minimum = ar[i+1] - ar[i]
    elif ar[i+1] - ar[i] == diff:
        num.append(ar[i+1])
        num.append(ar[i])
        
print ' '.join(map(str, sorted(num)))
