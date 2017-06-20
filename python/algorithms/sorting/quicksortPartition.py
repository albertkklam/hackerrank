# Quicksort - Partition
## https://www.hackerrank.com/challenges/quicksort1

def partition(ar):    
    p = ar[0]
    left = []
    equal = [p]
    right = []

    for i in range(1,len(ar)):
        if ar[i] < p:
            left.append(ar[i])
        elif ar[i] > p:
            right.append(ar[i])
        else:
            equal.append(ar[i])

    print ' '.join(map(str,left + equal + right))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)
