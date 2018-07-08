# Standardize Mobile Number Using Decorators
## https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
### Python 3.6

def wrapper(f):
    def fun(l):
        return f(["+91 {} {}".format(ll[len(ll) - 10:len(ll) - 5], ll[len(ll) - 5:]) for ll in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep="\n")

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
    
