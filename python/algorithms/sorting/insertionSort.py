# Insertion Sort
## https://www.hackerrank.com/challenges/insertionsort2

def insertionSort(ar):    
    for i in range(1,len(ar)):
        c,p = ar[i],i
        
        while p > 0 and ar[p-1] > c:           
            ar[p] = ar[p-1]
            p -= 1
            
        ar[p] = c
        print ' '.join(map(str,ar))  
        
m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
