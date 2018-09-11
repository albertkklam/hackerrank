# Mutations
## https://www.hackerrank.com/challenges/python-mutations/problem
### Python 2.7

string_list = [letter for letter in raw_input().strip()]
index, character = raw_input().strip().split()
string_list[int(index)] = character
print ''.join(string_list)
