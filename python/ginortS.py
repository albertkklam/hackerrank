# ginortS
## https://www.hackerrank.com/challenges/ginorts/problem
### Python 3.6

print(''.join(sorted(input(), key = lambda x: (not x.islower(), not x.isalpha(), x.isdigit() and int(x) % 2 == 0, x))))
