import sys

N, M = map(int, sys.stdin.readline().strip().split())

arr = []
ask = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

for _ in range(M):
    ask.append(list(map(int, sys.stdin.readline().strip().split())))

new_arr = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        new_arr[i][j] = new_arr[i-1][j] + new_arr[i][j-1] + arr[i-1][j-1] - new_arr[i-1][j-1]

for x1, y1, x2, y2 in ask:
    print(new_arr[x2][y2]-new_arr[x1-1][y2]-new_arr[x2][y1-1]+new_arr[x1-1][y1-1])