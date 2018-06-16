# Alternating Characters
## Alice has a binary string, B, of length n. 
## She thinks a binary string is beautiful if and only if it doesn't contain the substring "010".
## In one step, Alice can change a 0 to a 1 (or vice-versa). 
## Count and print the minimum number of steps needed to make Alice see the string as beautiful.

import re
n = int(raw_input().strip())
B = raw_input().strip()
B1 = re.sub('010','011',B)

print sum(B1[i] != B[i] for i in range(len(B1)))
