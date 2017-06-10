# HackerRank in a String!
## https://www.hackerrank.com/challenges/hackerrank-in-a-string

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    ind = []
    for h in 'hackerrank':
        if h in s:
            ind.append(1)
            s = s[s.index(h)+1:]
        else:
            break
    if sum(ind) == len('hackerrank'):
        print 'Yes'
    else:
        print 'No'
