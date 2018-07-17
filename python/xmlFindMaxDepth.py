# XML2 - Find the Maximum Depth
## https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem
### Python 3.6

import xml.etree.ElementTree as etree

maxDepth = 0


def depth(elem, level):
    global maxDepth
    if level == maxDepth:
        maxDepth += 1
    for child in elem:
        depth(child, level + 1)


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxDepth)
