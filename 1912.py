import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))

arr2 = []
before = 0
for i in arr:
    before = max(before+i, i)
    arr2.append(before)

print(max(arr2))
