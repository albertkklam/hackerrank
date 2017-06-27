# Electronics Shop
## https://www.hackerrank.com/challenges/electronics-shop

def getMoneySpent(keyboards, drives, s):
    return max([(k + d) for k in keyboards for d in drives if s >= (k + d)] + [-1])
    
s,n,m = raw_input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = map(int, raw_input().strip().split(' '))
drives = map(int, raw_input().strip().split(' '))

moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
