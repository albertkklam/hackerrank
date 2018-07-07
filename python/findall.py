# Re.findall() & Re.finditer()
## https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
### Python 3.6

import re
t = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})[qwrtypsdfghjklzxcvbnm]', input(), flags = re.IGNORECASE)
if t:
    print(*t, sep="\n")
else:
    print(-1)
    
