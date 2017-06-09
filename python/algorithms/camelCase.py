# CamelCase
## https://www.hackerrank.com/challenges/camelcase

import re
s = raw_input().strip()
len(re.findall(r"[A-Z]+",s))+1
