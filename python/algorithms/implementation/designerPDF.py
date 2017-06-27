# Designer PDF Viewer
## https://www.hackerrank.com/challenges/designer-pdf-viewer

from string import ascii_lowercase as al

h = map(int, raw_input().strip().split(' '))
word = raw_input().strip()

dic = dict([(al[i],h[i]) for i in range(len(h))])
print dic[max(word, key = lambda key: dic[key])] * len(word)
