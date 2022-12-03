import sys

N, M = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
arr2 = list()
for _ in range(M):
    arr2.append(map(int, sys.stdin.readline().strip().split()))
total = 0
new_arr = [0]
for i in arr:
    total += i
    new_arr.append(total)

for i, j in arr2:
    print(new_arr[j]-new_arr[i-1])