from collections import Counter
import sys

N, M = map(int, sys.stdin.readline().strip().split(" "))
S = []
answer = 0

for _ in range(N):
    S.append(str(sys.stdin.readline().strip()))
arr = Counter(S)

for _ in range(M):
    if arr.get(sys.stdin.readline().strip()) is not None:
        answer += 1

print(answer)