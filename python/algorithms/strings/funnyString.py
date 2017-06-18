# Funny String
## https://www.hackerrank.com/challenges/funny-string

def funnyString(s):
    comp = sum([1 if abs(ord(s[i]) - ord(s[i+1])) == abs(ord(s[-i-1]) - ord(s[-i-2])) else 0 for i in range(len(s)-1)])
    if comp == len(s) - 1:
        return 'Funny'
    else:
        return 'Not Funny'

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = funnyString(s)
    print(result)
