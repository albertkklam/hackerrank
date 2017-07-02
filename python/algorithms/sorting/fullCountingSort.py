# The Full Counting Sort
## https://www.hackerrank.com/challenges/countingsort4

n = int(raw_input().strip())
ar = []

for i in range(n):
    num, string = raw_input().strip().split(' ')
    
    if i < n/2:
        ar.append((int(num),'-'))
    else:
        ar.append((int(num),string))

sorted_ar = sorted(ar, key=lambda x: x[0]) 
print ''.join((str(string) + ' ') for num, string in sorted_ar)
