# Bot Saves Princess
## https://www.hackerrank.com/domains/ai/ai-introduction

def displayPathtoPrincess():
    N = int(input())
    for n in range(0, N):
        row = list(map(str,input().strip()))
        try:
            p = row.index('p')
            i = N // 2 - n
            j = N // 2 - p
            
            if i < 0:
                while i < 0:
                    print('DOWN')
                    i += 1
            if i > 0:
                while i > 0:
                    print('UP')
                    i -= 1
            if j < 0:
                while j < 0:
                    print('RIGHT')
                    j += 1
            if j > 0:
                while j > 0:
                    print('LEFT')
                    j -= 1
        except ValueError:
            pass

displayPathtoPrincess()
