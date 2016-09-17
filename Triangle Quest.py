# Triangle Quest
##  Print a numerical triangle of height N-1

for i in range(1,input()):
    print sum(map(lambda x: 10**x,range(0,i)))*i
