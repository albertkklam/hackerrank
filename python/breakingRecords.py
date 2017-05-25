# Breaking the Records
## https://www.hackerrank.com/challenges/breaking-best-and-worst-records

def getRecord(s):
    highs = [max(score) for score in [s[:i+1] for i in range(len(s))]]
    lows = [min(score) for score in [s[:i+1] for i in range(len(s))]]
    return [sum([1 for i,j in zip(s[1:], highs[:len(s)]) if i-j > 0]), sum([1 for i,j in zip(s[1:], lows[:len(s)]) if i-j < 0])]

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
result = getRecord(s)
print " ".join(map(str, result))
