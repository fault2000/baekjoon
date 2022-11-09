import sys
from collections import Counter

arr = list()
arr2 = list()
N, M = map(int, sys.stdin.readline().strip().split())
for _ in range(N):
    arr.append(sys.stdin.readline().strip())
for _ in range(M):
    arr2.append(sys.stdin.readline().strip())

arr3 = Counter(arr2)
cnt = 0
arr4 = list()

for i in arr:
    if arr3[i] != 0:
        cnt += 1
        arr4.append(i)

arr4.sort()
print(cnt)
for i in arr4:
    print(i)