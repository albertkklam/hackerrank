# nCr Table
## https://www.hackerrank.com/challenges/ncr-table/problem

for _ in range(int(raw_input().strip())):
    n = int(raw_input().strip())
    c = 1
    ans = []
    for k in range(1, n+2):
        ans.append(c%10**9)
        c = c * (n + 1 - k) / k
    print ' '.join(map(str, ans))
