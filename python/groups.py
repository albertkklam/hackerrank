# Group(), Groups() & Groupdict()
## https://www.hackerrank.com/challenges/re-group-groups/problem
### Python 3.6

import re
m = re.search(r"([a-zA-Z0-9])\1", input())
if m is not None:
    print(m.group(1))
else:
    print(-1)
    
