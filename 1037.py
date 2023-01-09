import sys

a = int(sys.stdin.readline().strip())
b = list(map(int, sys.stdin.readline().strip().split()))
b.sort()
print(b[0]*b[-1])