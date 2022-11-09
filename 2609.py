import sys

def Eudlidean(a, b):
    if b == 0:
        return a
    r = a%b
    return Eudlidean(b, r)

a, b = map(int, sys.stdin.readline().strip().split())
c = Eudlidean(a, b)
d = int((a*b)/c)
print(c)
print(d)