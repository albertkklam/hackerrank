# Running Time of Quicksort
## https://www.hackerrank.com/challenges/quicksort4

def quick_sort(ar, start, end):    
    
    count = 0
    if end - start <= 0:
        return 0
    else:
        p = ar[end]
        index = start
        
        for i in range(start, end):
            if ar[i] < p:
                ar[i], ar[index] = ar[index], ar[i]
                index += 1
                count += 1
                
        ar[index], ar[end] = ar[end], ar[index]
        count += 1
        
        l = quick_sort(ar, start, index-1)
        r = quick_sort(ar, index+1, end)
        
        return count + l + r
    
    
def insertion_sort(ar):
    count = 0
    for i in range(1,len(ar)):
        c,p = ar[i],i
        
        while p > 0 and ar[p-1] > c:           
            ar[p] = ar[p-1]
            p -= 1
            count += 1
            
        ar[p] = c
    return count

    
n = int(raw_input().strip())
arr1 = map(int,raw_input().strip().split())
arr2 = arr1[:]
print insertion_sort(arr1) - quick_sort(arr2, 0, n-1)
