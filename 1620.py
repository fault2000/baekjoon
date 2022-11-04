import sys

N, M = map(int, sys.stdin.readline().strip().split(" "))
arr = dict()

for i in range(1, N+1):
    arr[i]= sys.stdin.readline().strip()

for i in range(M):
    input = sys.stdin.readline().strip()
    if input.isdigit():
        print(arr[int(input)])
    else:
        print(next((index for index, name in arr.items() if name == input), None))