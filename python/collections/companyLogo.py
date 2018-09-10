# Company Logo
## https://www.hackerrank.com/challenges/most-commons/problem
### Python 3.6

string = input()
string_dict = {}
for s in string:
    if string_dict.get(s) is None:
        string_dict[s] = 1
    else:
        string_dict[s] += 1

for key, value in sorted(string_dict.items(), key=lambda x: (-x[1], x[0]))[:3]:
    print("{} {}".format(key, value))
