# Strange Grid Again
## https://www.hackerrank.com/challenges/strange-grid/problem

r,c = map(int, raw_input().strip().split(' '))
if (r % 2) == 1:
    print (r/2)*10 + (c-1)*2
else:
    print (r/2-1)*10 + 2*c - 1
