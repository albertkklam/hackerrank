# Repeated String
## Print the number of times the letter 'a' appears in the first n letters of a string that repeats a substring s an infinite number of times.

s = raw_input().strip()
n = long(raw_input().strip())

print s.count('a') * (n/len(s)) + s[:n % len(s)].count('a')
