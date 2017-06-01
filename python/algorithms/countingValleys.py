# Counting Valleys
## https://www.hackerrank.com/challenges/counting-valleys

n = int(raw_input())
string = list(str(raw_input().strip()))

pos = 0
valleys = 0

for s in string:
    if s == 'D':
        if pos == 0:
            valleys += 1
        pos -= 1
    else:
        pos += 1

print valleys
