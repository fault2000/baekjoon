import sys

def abc(a, b):
    if b == 0:
        return a
    return abc(b, a%b)

T = int(sys.stdin.readline())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().strip().split())
    if b>a:
        print(int((a*b)/abc(b, a)))
    else:
        print(int((a*b)/abc(a, b)))