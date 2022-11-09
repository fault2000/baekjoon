import sys

while True:
    a, b = map(int, sys.stdin.readline().strip().split())
    if (a != 0) and (b != 0):
        c = b/a
        if c.is_integer():
            print("factor")
        else:
            c = a/b
            if c.is_integer():
                print("multiple")
            else:
                print("neither")
    else:
        exit()