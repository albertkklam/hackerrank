# Anagram
## https://www.hackerrank.com/challenges/anagram

def anagram(s):
    if len(s) % 2 != 0:
        return -1
    else:
        return sum([abs(s[:len(s)/2].count(char) - s[len(s)/2:].count(char)) for char in set(s)]) / 2

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = anagram(s)
    print(result)
