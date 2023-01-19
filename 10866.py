import sys, collections

N = int(sys.stdin.readline())
Deque = collections.deque()
for _ in range(N):
    ins = sys.stdin.readline().strip().split()
    if ins[0] == "push_front":
        Deque.appendleft(ins[1])
    elif ins[0] == "push_back":
        Deque.append(ins[1])
    elif ins[0] == "pop_front":
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque.popleft())
    elif ins[0] == "pop_back":
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque.pop())
    elif ins[0] == "size":
        print(len(Deque))
    elif ins[0] == "empty":
        if len(Deque) == 0:
            print(1)
        else:
            print(0)
    elif ins[0] == "front":
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque[0])
    elif ins[0] == "back":
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque[-1])
