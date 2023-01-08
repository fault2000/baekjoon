import collections

N, K = map(int, input().strip().split())
queue = collections.deque()
ans = []

for i in range(N):
    queue.append(i)

while len(queue) != 0:
    for _ in range(K-1):
        tmp = queue.popleft()
        queue.append(tmp)
    tmp = queue.popleft()
    ans.append(tmp+1)

if len(ans) == 1:
    print("<", ans[0], ">", sep="")
else:
    for i in range(len(ans)):
        if i == 0:
            print("<", ans[i], ", ", sep="", end="")
        elif i == len(ans)-1:
            print(ans[i], ">", sep="")
        else:
            print(ans[i], ", ", sep="", end="")