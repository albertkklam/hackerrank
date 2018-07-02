# Any or All
## https://www.hackerrank.com/challenges/any-or-all/problem
### Python 3.6

n = int(input())
num = list(map(int, input().split(' ')))
if (all([_ > 0 for _ in num])):
    print(any([_ == int(str(_)[::-1]) for _ in num]))
else:
    print(False)
    
