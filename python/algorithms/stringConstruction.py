# String Construction
## https://www.hackerrank.com/challenges/string-construction

def stringConstruction(s):
    return len(set(s))

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = stringConstruction(s)
    print(result)
