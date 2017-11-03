# Restaurant
## https://www.hackerrank.com/challenges/restaurant/problem

import math
for _ in range(int(raw_input().strip())):
    l, b = map(int, raw_input().strip().split(' '))
    divisors = {s: l*b / s for s in range(1, l*b+1) if (l*b) % s == 0 and math.sqrt(s).is_integer() and float(l/math.sqrt(s)).is_integer() and float(b/math.sqrt(s)).is_integer()}
    max_key = max(divisors.keys())
    print max({value for key, value in divisors.items() if key == max_key})
