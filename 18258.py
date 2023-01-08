import sys, collections

N = int(sys.stdin.readline())
queue = collections.deque()

for _ in range(N):
    ins = sys.stdin.readline().strip()
    if ins[0:4] == "push":
        queue.append(int(ins[5:]))
    elif ins == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif ins == "size":
        print(len(queue))
    elif ins == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif ins == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif ins == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
