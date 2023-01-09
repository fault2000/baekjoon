import sys

n = int(sys.stdin.readline())
arr = [0]

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr2 = [0 for _ in range(n+1)]

if n == 1:
    print(arr[1])
elif n == 2:
    print(arr[1]+arr[2])
else:
    arr2[1] = arr[1]
    arr2[2] = arr[1] + arr[2]
    arr2[3] = max(arr[1] + arr[3], arr[2] + arr[3])
    for i in range(4, n+1):
        arr2[i] = max(arr2[i-3] + arr[i-1] + arr[i], arr2[i-2] + arr[i])
    print(arr2[n])

