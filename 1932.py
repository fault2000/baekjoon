import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(1, n):
    tempArr = []
    for j in range(len(arr[i])):
        if j==0:
            tempArr.append(arr[i][j]+arr[i-1][j])
        elif j==len(arr[i])-1:
            tempArr.append(arr[i][j]+arr[i-1][j-1])
        else:
            tempArr.append(arr[i][j]+max(arr[i-1][j-1], arr[i-1][j]))
    arr[i] = tempArr

print(max(arr[n-1]))