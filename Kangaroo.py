# Kangaroo
## There are two kangaroos on an x-axis ready to jump in the positive direction (i.e, toward positive infinity). The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump. The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump. Given the starting locations and movement rates for each kangaroo, can you determine if they'll ever land at the same location at the same time?

x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

score1 = x1
score2 = x2

if x1 <= x2 and v1 > v2:
    while score1 < score2:
        score1 += v1
        score2 += v2
    
elif x1 >= x2 and v1 < v2:
    while score1 > score2:
        score1 += v1
        score2 += v2

if score1 == score2:
    print 'YES'
else:
    print 'NO'
