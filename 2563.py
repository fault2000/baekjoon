import sys

arr = [[0 for _ in range(100)] for _ in range(100)]
cnt = 0
N = int(sys.stdin.readline())
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split(" "))
    for i in range(b, b+10):
        for j in range(a, a+10):
            if arr[i][j] == 1:
                continue
            else:
                arr[i][j] = 1
                cnt += 1

print(cnt)