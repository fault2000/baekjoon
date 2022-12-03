import sys

N, M = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
new_dict = {0: 1}
total = 0

for i in range(1, M):
    new_dict[i] = 0

for i in arr:
    total += i
    new_dict[total%M] += 1

ans = 0

for i in range(M):
    temp = new_dict[i]
    if temp>1:
        ans += (temp*(temp-1))//2


print(ans)