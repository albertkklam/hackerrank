# Mars Exploration
## https://www.hackerrank.com/challenges/mars-exploration

S = raw_input().strip()
print sum([1 if S[i] != ('SOS' * (len(S) / 3))[i] else 0 for i in range(len(S))])
