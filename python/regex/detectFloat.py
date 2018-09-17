# Detect Floating Point Number
## https://www.hackerrank.com/challenges/introduction-to-regex/problem
### Python 3.6

import re

t = int(input().strip())
for _ in range(t):
    string = input().strip()
    if re.match("^[\-\+]?[\d]*[\.][\d]+$", string) is not None:
        try:
            float(string)
            print("True")
        except:
            print("False")
    else:
        print("False")
        
