import sys

def RGBMin(arr):
    output = []
    output.append(min(arr[0][1], arr[0][2])+arr[1][0])
    output.append(min(arr[0][0], arr[0][2])+arr[1][1])
    output.append(min(arr[0][0], arr[0][1])+arr[1][2])
    return output

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    RGB = list(map(int, sys.stdin.readline().strip().split()))
    arr.append(RGB)
    
for i in range(1, N):
    arr[i] = RGBMin([arr[i-1], arr[i]])

print(min(arr[N-1]))