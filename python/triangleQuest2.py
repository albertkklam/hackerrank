# Triangle Quest 2
## Given a positive integer N, print a palindromic triangle of size N

for i in range(1,int(raw_input())+1):
    print sum(map(lambda x: 10**x,range(0,i)))**2
