#하다가 때려침 주의
import sys

N, M, K = map(int, sys.stdin.readline().strip().split())

arr = []
comp = {"B": True, "W": False}

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

B = [[0 for _ in range(N+1)] for _ in range(N+1)]
W = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        B[i][j] = B[i-1][j] + B[i][j-1] - B[i-1][j-1] + (0 if arr[i-1][j-1]=="B" else 0)

for x1, y1, x2, y2 in ask:
    print(new_arr[x2][y2]-new_arr[x1-1][y2]-new_arr[x2][y1-1]+new_arr[x1-1][y1-1])