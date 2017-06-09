# Caesar Cipher
## https://www.hackerrank.com/challenges/caesar-cipher-1

from string import ascii_lowercase as al

n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())

S = []

for char in s:
    if char.islower(): 
        S.append(al[(al.index(char)+k)%26])
    elif char.isupper():
        S.append(al[(al.index(char.lower())+k)%26].upper())
    else:
        S.append(char)
        
print ''.join(S)
