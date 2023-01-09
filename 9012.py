import sys

T = int(sys.stdin.readline())

for _ in range(T):
    arr = []
    check = True
    VPS = sys.stdin.readline().strip()
    for i in VPS:
        if i == "(":
            arr.append(i)
        else:
            if len(arr) == 0:
                check = False
                break
            else:
                arr.pop()
    if not len(arr) == 0 or not check:
        print("NO")
    else:
        print("YES")

