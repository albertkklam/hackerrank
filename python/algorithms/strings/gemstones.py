# Gemstones
## https://www.hackerrank.com/challenges/gem-stones

def gemstones(arr):
    return len(set.intersection(*map(set, arr)))

n = int(raw_input().strip())
arr = []
arr_i = 0
for arr_i in xrange(n):
    arr_t = str(raw_input().strip())
    arr.append(arr_t)
result = gemstones(arr)
print(result)
