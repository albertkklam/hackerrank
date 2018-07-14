# Athlete Sort
## https://www.hackerrank.com/challenges/python-sort-sort/problem
### Python 3.6

if __name__ == '__main__':
    n, m = map(int, input().split(' '))
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    for arrays in sorted(arr, key = lambda x: x[k]):
        print(" ".join(map(str, arrays)))
        
