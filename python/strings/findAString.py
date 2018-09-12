# Find a string
## https://www.hackerrank.com/challenges/find-a-string/problem
### Python 2.7

string,substring = (raw_input().strip() for _ in range(2))
[string[n:n+len(substring)] for n in range(0,len(string))].count(substring)
