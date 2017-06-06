# Beautiful Days at the Movies
## https://www.hackerrank.com/challenges/beautiful-days-at-the-movies

i,j,k = map(int, raw_input().strip().split(' '))
print sum([1 for num in range(i,j+1) if abs(num - int(str(num)[::-1]))%k == 0])
