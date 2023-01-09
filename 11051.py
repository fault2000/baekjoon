import sys

sys.setrecursionlimit(10**6)

N, K = map(int, sys.stdin.readline().strip().split())
arr = [[0 for _ in range(1001)] for _ in range(1001)]

def abc(n, k):
    if arr[n][k] != 0:
        return arr[n][k]
    if n == k or k == 0:
        arr[n][k] = 1
        return 1
    else:
        a = abc(n-1, k-1) + abc(n-1, k)
        arr[n][k] = a
        return a

print(abc(N, K)%10007)