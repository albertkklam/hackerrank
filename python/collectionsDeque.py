# Collections.deque()
## https://www.hackerrank.com/challenges/py-collections-deque/problem
### Python 3.6

from collections import deque
n = int(input())
d = deque()

for _ in range(n):
    task = input().split(' ')
    if len(task) > 1:
        operation, num = task
        if operation == "append":
            d.append(int(num))
        else:
            d.appendleft(int(num))
    else:
        if task[0] == "pop":
            d.pop()
        else:
            d.popleft()

print(' '.join([str(_) for _ in d]))
