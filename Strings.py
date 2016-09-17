# Mutations

string_list = [letter for letter in raw_input().strip()]
index, character = raw_input().strip().split()
string_list[int(index)] = character
print ''.join(string_list)

# Find a string
string,substring = (raw_input().strip() for _ in range(2))
[string[n:n+len(substring)] for n in range(0,len(string))].count(substring)
