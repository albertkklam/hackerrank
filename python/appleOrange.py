# Apple and Orange
## https://www.hackerrank.com/challenges/apple-and-orange

s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))

print len([a + apple_distance for apple_distance in apple if (apple_distance >= s - a) & (apple_distance <= t - a)])
print len([b + orange_distance for orange_distance in orange if (orange_distance <= t - b) & (orange_distance >= s - b)])
