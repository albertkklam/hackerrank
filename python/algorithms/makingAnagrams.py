# Making Anagrams
## https://www.hackerrank.com/challenges/making-anagrams

def makingAnagrams(s1, s2):
    return sum([abs(s1.count(char) - s2.count(char)) for char in set(s1+s2)])

s1 = raw_input().strip()
s2 = raw_input().strip()
result = makingAnagrams(s1, s2)
print(result)
