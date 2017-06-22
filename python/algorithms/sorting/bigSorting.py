# Big Sorting
## https://www.hackerrank.com/challenges/big-sorting

n = int(raw_input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in xrange(n):
    unsorted_t = str(raw_input().strip())
    unsorted.append(unsorted_t)
    
sorted_list = sorted(unsorted, key = int)
for num in sorted_list:
    print num
