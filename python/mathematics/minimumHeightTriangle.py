# Minimum Height Triangle
## https://www.hackerrank.com/challenges/lowest-triangle

import math
def lowestTriangle(base, area):
    return int(math.ceil(area / (base / 2.0)))

base, area = raw_input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)
