# Validating UID
## https://www.hackerrank.com/challenges/validating-uid/problem
### Python 3.6

import re

t = int(input())
for _ in range(t):
    string = input().strip()
    if re.match(r"(?!.*(.).*\1)(?=(?:[a-zA-Z0-9]*[A-Z]){2,})(?=(?:[a-zA-Z0-9]*[0-9]){3,})[a-zA-Z0-9]{10}", string):
        print("Valid")
    else:
        print("Invalid")
        
