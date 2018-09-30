# Validating Credit Card Numbers
## https://www.hackerrank.com/challenges/validating-credit-card-number/problem
### Python 3.6

import re

t = int(input())
for _ in range(t):
    string = input().strip()
    if re.match(r"(?!(.)*\1{3,})^[456]\d{15}$", string):
        print("Valid")
    elif "-" in string and re.match(r"^[456]\d{3}(-\d{4}){3}$", string):
        new_string = string.replace("-","")
        if re.match(r"(?!(.)*\1{3,})^[456]\d{15}$", new_string):
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")
