# Pangrams
## Print whether a given string is a pangram or not. Pangrams are sentences constructed by using every letter of the alphabet at least once.

from string import ascii_lowercase as al

s = set(raw_input().strip().lower()) - set(' ')
if set(al) == set(s):
    print 'pangram'
else: 
    print 'not pangram'
