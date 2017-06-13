# Love-Letter Mystery
## https://www.hackerrank.com/challenges/the-love-letter-mystery

def theLoveLetterMystery(s):
    return sum([abs(ord(s[i])-ord(s[::-1][i])) for i in range(len(s) / 2)])

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = theLoveLetterMystery(s)
    print(result)
