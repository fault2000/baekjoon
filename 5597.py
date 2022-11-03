import sys

a = list(range(1, 31))

for _ in range(28):
    b = int(sys.stdin.readline())
    a.remove(b)

for i in a:
    print(i)