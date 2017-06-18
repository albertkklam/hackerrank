# Two Strings
## https://www.hackerrank.com/challenges/two-strings

def twoStrings(s1, s2):
    if bool(set(s1).intersection(set(s2))):
        return 'YES'
    else:
        return 'NO'

q = int(raw_input().strip())
for a0 in xrange(q):
    s1 = raw_input().strip()
    s2 = raw_input().strip()
    result = twoStrings(s1, s2)
    print(result)
