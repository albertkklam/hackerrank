# Utopian Tree
## https://www.hackerrank.com/challenges/utopian-tree

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    height = 1
    m = 0
    while m < n:
        if m%2 == 1:
            height += 1
        else:
            height *= 2
        m += 1
    print height
