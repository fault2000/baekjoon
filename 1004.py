import sys

def get_len(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)

T = int(sys.stdin.readline())

for _ in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    n = int(sys.stdin.readline())
    arr = list()
    for _ in range(n):
        arr.append(list(map(int, sys.stdin.readline().strip().split())))
    output = 0

    for i in arr:
        if (get_len(x1, y1, i[0], i[1]) < i[2]) ^ (get_len(x2, y2, i[0], i[1]) < i[2]):
            output += 1
    
    print(output)


