# Re.start() & Re.end()
## https://www.hackerrank.com/challenges/re-start-re-end/problem
### Python 3.6

import re

string = input()
substring = input()
m = re.search(substring, string)
if m is None:
    print((-1,-1))
else:
    index = 0
    while index + len(substring) < len(string):
        print((index + m.start(), index + m.end() - 1))
        index += m.start() + 1
        m = re.search(substring, string[index:])
