# Game of Thrones
## https://www.hackerrank.com/challenges/game-of-thrones

def gameOfThrones(s):
    if [s.count(char) % 2 for char in set(s)].count(1) <= 1:
        return 'YES'
    else:
        return 'NO'

s = raw_input().strip()
result = gameOfThrones(s)
print(result)
