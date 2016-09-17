# CamelCase
## Find the number of words in a CamelCase string. CamelCase strings are StringsLikeThis.

import re
s = raw_input().strip()
len(re.findall(r"[A-Z]+",s))+1
