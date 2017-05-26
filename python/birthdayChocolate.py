# Birthday Chocoloate
## https://www.hackerrank.com/challenges/the-birthday-bar

def solve(n, s, d, m):
    return len([1 for i in range(n-m+1) if sum(s[i:i+m]) == d])

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
