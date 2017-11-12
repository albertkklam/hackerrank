# Halloween Party
## https://www.hackerrank.com/challenges/halloween-party/problem

for _ in range(int(raw_input().strip())):
    k = int(raw_input().strip())
    if k%2 == 0:
        print (k/2) * (k/2)
    else:
        print (k/2) * (k/2 + 1)
