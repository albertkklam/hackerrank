# Word Order
## https://www.hackerrank.com/challenges/word-order/problem
### Python 3.6

from collections import OrderedDict

n = int(input())
word_dict = OrderedDict()

for _ in range(n):
    string = input().rstrip()
    if word_dict.get(string) is None:
        word_dict[string] = 1
    else:
        word_dict[string] += 1

print(len(word_dict.keys()))
print(*word_dict.values())
