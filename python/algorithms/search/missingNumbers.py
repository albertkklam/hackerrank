# Missing Numbers
## https://www.hackerrank.com/challenges/missing-numbers

n = int(raw_input().strip())
A = map(int, raw_input().strip().split(' '))
m = int(raw_input().strip())
B = map(int, raw_input().strip().split(' '))

missing = []
for num in set(B):
    if B.count(num) > A.count(num):
        missing.append(num)
        
print ' ' .join(map(str, missing))
