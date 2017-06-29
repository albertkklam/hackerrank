# Quicksort In-Place
## https://www.hackerrank.com/challenges/quicksort3

def quick_sort(ar, start, end):    

    if end - start <= 0:
        return ar
    else:
        p = ar[end]
        index = start
        
        for i in range(start, end):
            if ar[i] < p:
                ar[i], ar[index] = ar[index], ar[i]
                index += 1
                
        ar[index], ar[end] = ar[end], ar[index]
        print ' '.join(map(str, ar))
        
        ar = quick_sort(ar, start, index-1)
        ar = quick_sort(ar, index+1, end)
        
        return ar
    
n = int(raw_input().strip())
ar = [int(i) for i in raw_input().strip().split()]
quick_sort(ar, 0, n-1)
