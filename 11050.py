import sys

N, K = map(int, sys.stdin.readline().strip().split())
total = 1

def abc(n, k):
    if n == k or k == 0:
        return 1
    else:
        return abc(n-1, k-1) + abc(n-1, k)

print(abc(N, K))