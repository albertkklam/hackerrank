# Counting Sort 2
## https://www.hackerrank.com/challenges/countingsort2

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
counts = [(i, ar.count(i)) for i in range(100)]
print ''.join((str(num) + ' ') * count for num, count in counts)
