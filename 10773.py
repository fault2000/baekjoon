import sys

arr = []

K = int(sys.stdin.readline())

for _ in range(K):
    a = int(sys.stdin.readline())
    if a==0:
        arr.pop()
    else:
        arr.append(a)

print(sum(arr))