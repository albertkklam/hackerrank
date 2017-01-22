# collections.Counter()
## https://www.hackerrank.com/challenges/collections-counter

shoes = int(raw_input())
sizes = map(int, raw_input().split())
money = 0
for i in range(int(raw_input())):
    shoe_price = map(int, raw_input().split())
    if shoe_price[0] in sizes:
        sizes.remove(shoe_price[0])
        money += shoe_price[1]

print money
