# Merge the Tools
## https://www.hackerrank.com/challenges/merge-the-tools

s = map(str,raw_input().strip())
k = int(raw_input().strip())

subList = [''.join(sorted(set(s[i:i+k]),key=s[i:].index)) for i in range(0,len(s),k)]
print '\n'.join(subList)
