# Migratory Birds
## https://www.hackerrank.com/challenges/migratory-birds

n = int(raw_input().strip())
types = map(int, raw_input().strip().split(' '))
print [key for key,counts in [(t,types.count(t)) for t in set(types)] if counts == max([types.count(t) for t in set(types)])][0]
