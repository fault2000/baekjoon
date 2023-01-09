import collections, sys

N = int(sys.stdin.readline())
router = collections.deque()

while(True):
    packet = int(sys.stdin.readline())
    if packet == -1:
        break
    if packet == 0:
        if len(router) != 0:
            router.popleft()
    elif len(router) == N:
        continue
    else:
        router.append(packet)

if len(router) == 0:
    print("empty")
else:
    for i in router:
        print(i, end=" ")