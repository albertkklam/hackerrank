# Find the Point
## https://www.hackerrank.com/challenges/find-point

for _ in range(int(raw_input().strip())):
    px, py, qx, qy = [int(_) for _ in raw_input().strip().split()]
    print (qx - px) + qx, (qy - py) + qy
