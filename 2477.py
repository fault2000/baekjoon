import sys

K = int(sys.stdin.readline().strip())
arr = list()
for _ in range(6):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

if arr[0][0] == arr[2][0] and arr[1][0] == arr[-1][0]:
    print((arr[3][1]*arr[4][1]-arr[0][1]*arr[1][1])*K)
elif arr[0][0] == arr[-2][0] and arr[1][0] == arr[-1][0]:
    print((arr[2][1]*arr[3][1]-arr[0][1]*arr[-1][1])*K)
elif arr[0][0] == arr[-2][0] and arr[-1][0] == arr[-3][0]:
    print((arr[1][1]*arr[2][1]-arr[-2][1]*arr[-1][1])*K)
else:
    for i in range(4):
        if arr[i][0] == arr[i+2][0]:
            a = arr[i+1][1]*arr[i+2][1]
            del arr[i:i+4]
            print((arr[0][1]*arr[1][1]-a)*K)
            exit()

