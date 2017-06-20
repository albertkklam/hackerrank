# Running Time of Algorithms
## https://www.hackerrank.com/challenges/runningtime

def runningTime(ar):
    count = 0
    for i in range(1,len(ar)):
        c,p = ar[i],i
        
        while p > 0 and ar[p-1] > c:           
            ar[p] = ar[p-1]
            p -= 1
            count += 1
            
        ar[p] = c
    print count
        
m = input()
ar = [int(i) for i in raw_input().strip().split()]
runningTime(ar)
