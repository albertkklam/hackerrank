# Army Game
## https://www.hackerrank.com/challenges/game-with-cells

import math
n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
print int(math.ceil(n/2.0) * math.ceil(m/2.0))
