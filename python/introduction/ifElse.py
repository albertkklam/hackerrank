# Python If-Else
## https://www.hackerrank.com/challenges/py-if-else/problem
### Python 3.6

N = int(input())
if N % 2 == 1 or (N % 2 == 0 and 6 <= N <= 20):
    print("Weird")
elif N % 2 == 0 and (2 <= N <= 5 or N > 20):
    print("Not Weird")

if __name__ == '__main__':
    N = int(input())
