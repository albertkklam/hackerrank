# Pangrams
## https://www.hackerrank.com/challenges/pangrams

from string import ascii_lowercase as al

s = set(raw_input().strip().lower()) - set(' ')
if set(al) == set(s):
    print 'pangram'
else: 
    print 'not pangram'
