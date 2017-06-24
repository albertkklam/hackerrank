# Counting Sort 1
## https://www.hackerrank.com/challenges/countingsort1

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
counts = [ar.count(i) for i in range(100)]
print ' '.join(map(str, counts))
