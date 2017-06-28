# Find Digits
## https://www.hackerrank.com/challenges/find-digits

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print sum([1 for x in [int(x) for x in str(n) if int(x) != 0] if n%x == 0])
