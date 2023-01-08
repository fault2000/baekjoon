import sys

n = int(sys.stdin.readline())
stack = []
high = 0
check = True
output = []

for _ in range(n):
    tmp = int(sys.stdin.readline())
    if tmp > high:
        for i in range(high, tmp):
            stack.append(i)
            output.append("+")
        high = tmp
        stack.pop()
        output.append("-")
    else:
        if stack.pop() != tmp-1:
            check = False
            break
        else:
            output.append("-")

if check:
    for i in output:
        print(i)
else:
    print("NO")