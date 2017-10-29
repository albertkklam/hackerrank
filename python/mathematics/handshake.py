# Handshake
## https://www.hackerrank.com/challenges/handshake

T = int(raw_input().strip())
for a0 in xrange(T):
    N = int(raw_input().strip())
    print N * (N - 1) / 2
