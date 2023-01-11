import sys

N = int(sys.stdin.readline())
arr = []
white = 0
blue = 0
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

def square(x, y, n):
    global white, blue
    first = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if first != arr[i][j]:
                square(x, y, n//2)
                square(x+n//2, y, n//2)
                square(x, y+n//2, n//2)
                square(x+n//2, y+n//2, n//2)
                return
    if first == 0:
        white += 1
        return
    else:
        blue += 1
        return
square(0, 0, N)
print(white)
print(blue)