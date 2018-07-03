# Re.split()
## https://www.hackerrank.com/challenges/re-split/problem
### Python 3.6

regex_pattern = r"\.|\,"
import re
print("\n".join(re.split(regex_pattern, input())))
