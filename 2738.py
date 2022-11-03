import sys

N, M = map(int, sys.stdin.readline().split(" "))

A = list()
B = list()

for _ in range(N):
    A.append(sys.stdin.readline().strip().split(" "))

for _ in range(N):
    B.append(sys.stdin.readline().strip().split(" "))

C = list()
for i, j in zip(A, B):
    arr = list()
    for k, l in zip(i, j):
        arr.append(int(k)+int(l))
    C.append(arr)

for i in C:
    for j in i:
        print(j, end=" ")
    print()