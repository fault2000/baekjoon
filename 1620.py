import sys

N, M = map(int, sys.stdin.readline().strip().split(" "))
arr = dict()
arr2 = dict()

for i in range(1, N+1):
    input=sys.stdin.readline().strip()
    arr[i]= input
    arr2[input] = i

for i in range(M):
    input = sys.stdin.readline().strip()
    if input.isdigit():
        print(arr[int(input)])
    else:
        print(arr2[input])