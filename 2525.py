import sys
A, B = map(int, sys.stdin.readline().strip().split(" "))
C = int(sys.stdin.readline())
a = int(C/60)
b = int(C%60)
e = 0
if B+b >= 60:
    e = (B+b)/60
    E = (B+b)%60
else:
    E = B+b
D = (A+a+e)%24

print(int(D), int(E))
