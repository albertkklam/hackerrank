# Jumping on the Clouds: Revisited
## https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
c = map(int,raw_input().strip().split(' '))
print 100 - sum([1 if x == 0 else 3 for x in [c[i] for i in range(n) if i%k == 0]])
