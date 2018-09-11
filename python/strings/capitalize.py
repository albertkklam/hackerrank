# Capitalize!
## https://www.hackerrank.com/challenges/capitalize/problem
### Python 2.7

s = raw_input()

for word in s.split():
    s=s.replace(word,word.capitalize())

print s
