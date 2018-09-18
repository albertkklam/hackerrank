# Validating and Parsing Email Addresses
## https://www.hackerrank.com/challenges/validating-named-email-addresses/problem
### Python 3.6

import re
import email.utils

n = int(input())
for _ in range(n):
    string = email.utils.parseaddr(input().strip())
    name_string, email_string = string
    if bool(re.match("^[a-zA-Z][\w\-._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$", email_string)):
        print(email.utils.formataddr((name_string, email_string)))
