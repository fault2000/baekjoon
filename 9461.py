import sys

T = int(sys.stdin.readline())
for _ in range(T):
    arr = []
    arr.append(1)
    arr.append(1)
    arr.append(1)
    arr.append(2)
    arr.append(2)
    N = int(sys.stdin.readline())
    try:
        print(arr[N-1])
    except IndexError:
        for i in range(5, N):
            arr.append(arr[i-1]+arr[i-5])
        print(arr[N-1])
 