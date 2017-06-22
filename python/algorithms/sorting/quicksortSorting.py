# Quicksort 2 - Sorting
## https://www.hackerrank.com/challenges/quicksort2

def quick_sort(ar):    

    if len(ar) < 2:
        return ar
    else:
        p = ar[0]
        left, equal, right = [], [p], []

        for i in range(1,len(ar)):
            if ar[i] < p:
                left.append(ar[i])
            elif ar[i] > p:
                right.append(ar[i])
            else:
                equal.append(ar[i])

        ar = quick_sort(left) + equal + quick_sort(right)
        print ' '.join(map(str, ar))
        
        return ar
    
m = input()
ar = [int(i) for i in raw_input().strip().split()]
quick_sort(ar)
