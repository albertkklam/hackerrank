# Capitalize!
## Capitalize each word of a string s

s = raw_input()

for word in s.split():
    s=s.replace(word,word.capitalize())

print s
