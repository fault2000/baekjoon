import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(sys.stdin.readline().strip())

def square(x, y, n):
    global white, blue
    first = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if first != arr[i][j]:
                return "(" + square(x, y, n//2) + square(x, y+n//2, n//2) + square(x+n//2, y, n//2) + square(x+n//2, y+n//2, n//2) + ")"
    if first == "0":
        return "0"
    else:
        return "1"

print(square(0, 0, N))