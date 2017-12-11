# Bot Saves Princess 2
## https://www.hackerrank.com/challenges/saveprincess2?hr_b=1

def nextMove(n, r, c, grid):
    for nn in range(n):
        try:
            p = grid[nn].index('p')
            i = r - nn
            j = c - p
            
            if (i != 0):
                if i < 0:
                    print('DOWN')
                else:
                    print('UP')

            else:
                if j < 0:
                    print('RIGHT')
                else:
                    print('LEFT')
                
        except ValueError:
            pass
        
n = int(input().strip())
r,c = list(map(int, input().strip().split()))
grid = []
for i in range(0, n):
    grid.append(input())

nextMove(n,r,c,grid)
