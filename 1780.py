import sys

N = int(sys.stdin.readline())
arr = []
minus = 0
zero = 0
one = 0
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

def square(x, y, n):
    global minus, zero, one
    first = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if first != arr[i][j]:
                square(x, y, n//3)
                square(x, y+n//3, n//3)
                square(x, y+n*2//3, n//3)
                square(x+n//3, y, n//3)
                square(x+n//3, y+n//3, n//3)
                square(x+n//3, y+n*2//3, n//3)
                square(x+n*2//3, y, n//3)
                square(x+n*2//3, y+n//3, n//3)
                square(x+n*2//3, y+n*2//3, n//3)
                return
    if first == 0:
        zero += 1
        return
    elif first == -1:
        minus += 1
        return
    else:
        one += 1
        return
square(0, 0, N)
print(minus)
print(zero)
print(one)