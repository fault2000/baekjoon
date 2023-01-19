import sys, collections

N, M = map(int, sys.stdin.readline().strip().split())
loc = list(map(int, sys.stdin.readline().strip().split()))

queue = collections.deque(i for i in range(1, N+1))
cnt = 0

for i in loc:
    while queue[0] != i:
        if queue.index(i) > len(queue)//2:
            tmp = queue.pop()
            queue.appendleft(tmp)
            cnt += 1
        else:
            tmp = queue.popleft()
            queue.append(tmp)
            cnt += 1
    queue.popleft()

print(cnt)
    