import sys, re

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    ins = sys.stdin.readline().strip()
    if ins[0:4] == "push":
        arr.append(int(re.sub(r'[^0-9]', '', ins)))
    elif ins == "pop":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
    elif ins == "size":
        print(len(arr))
    elif ins == "empty":
        if len(arr):
            print(0)
        else:
            print(1)
    elif ins == "top":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[len(arr)-1])
    
