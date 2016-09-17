# Find a string
## Find the number of times a substring appears in a string

string,substring = (raw_input().strip() for _ in range(2))
[string[n:n+len(substring)] for n in range(0,len(string))].count(substring)
