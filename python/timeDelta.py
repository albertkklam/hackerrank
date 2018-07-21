# Time Delta
## https://www.hackerrank.com/challenges/python-time-delta/problem
### Python 3.6

from datetime import datetime, timedelta


def time_delta(t1, t2):
    return int(abs(t1 - t2).total_seconds())


if __name__ == '__main__':
    t = int(input())
    fmt = '%a %d %b %Y %H:%M:%S %z'
    for t_itr in range(t):
        t1 = datetime.strptime(input(), fmt)
        t2 = datetime.strptime(input(), fmt)
        delta = time_delta(t1, t2)
        print(delta)
        
