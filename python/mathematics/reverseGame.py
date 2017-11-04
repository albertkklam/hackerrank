# Reverse Game
## https://www.hackerrank.com/challenges/reverse-game/problem

for _ in range(int(raw_input().strip())):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    if k > n/2 - 1:
        print 2 * (n - k - 1)
    else:
        print 2 * k + 1
