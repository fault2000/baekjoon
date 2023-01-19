import sys, collections

T = int(sys.stdin.readline())

for _ in range(T):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    check = True
    queue = collections.deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    Rev = False
    if n == 0:
        queue = []

    for i in p:
        if i == "R":
            Rev = not Rev
        elif i == "D":
            if len(queue) == 0:
                check = False
                break
            else:
                if Rev:
                    tmp = queue.pop()
                else:
                    tmp = queue.popleft()
    if check:
        if Rev:
            queue.reverse()
            print("[" + ",".join(queue) + "]")
        else:
            print("[" + ",".join(queue) + "]")
    else:
        print("error")
    