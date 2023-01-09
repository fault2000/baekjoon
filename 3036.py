import sys

def abc(a, b):
    if b == 0:
        return a
    return abc(b, a%b)

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().strip().split()))

for i in range(1, N):
    div = 0
    if arr[0]>arr[i]:
        div = abc(arr[0], arr[i])
    else:
        div = abc(arr[i], arr[0])
    print(arr[0]//div, "/", arr[i]//div, sep="")


