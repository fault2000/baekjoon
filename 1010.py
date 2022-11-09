import sys

input = sys.stdin.readline

arr = [[0 for _ in range(31)] for _ in range(31)]

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

T = int(input())
for _ in range(T):
    N, M = map(int, input().strip().split())
    print(abc(M, N))