# Validating Email Addresses With a Filter 
## https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
### Python 3.6

import re

def fun(s):
    return bool(re.match("^[\w-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{1,3}$", s))

def filter_mail(emails):
    return list(filter(fun, emails))

n = int(input())
emails = []
for _ in range(n):
    emails.append(input())
filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
