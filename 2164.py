import collections

N = int(input())
queue = collections.deque()

for i in range(1, N+1):
    queue.append(i)

while(len(queue)!=1):
    queue.popleft()
    temp = queue.popleft()
    queue.append(temp)

print(queue.pop())