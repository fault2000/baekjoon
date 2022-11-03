import sys

a = list(map(int, sys.stdin.readline().strip().split(" ")))
b = [1, 1, 2, 2, 2, 8]
c = []
for i, j in zip(a, b):
    c.append(j-i)
for i in c:
    print(i, end=' ')