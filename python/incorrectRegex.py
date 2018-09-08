# Incorrect Regex
## https://www.hackerrank.com/challenges/incorrect-regex/problem
### Python 3.6

import re

for _ in range(int(input())):
    try:
        re.compile(input())
        print(True)
    except:
        print(False)
