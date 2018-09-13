# Piling Up!
## https://www.hackerrank.com/challenges/piling-up/problem
### Python 3.6

t = int(input())
for _ in range(t):
    n = int(input())
    cubes = list(map(int, input().split(' ')))
    print_me = "Yes"
    while len(cubes) > 1:
        if cubes[0] >= cubes[1]:
            cubes.pop(0)
            continue
        if cubes[-1] >= cubes[-2]:
            cubes.pop()
            continue
        print_me = "No"
        break
    print(print_me)
