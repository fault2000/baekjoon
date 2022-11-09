import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().strip().split())
A = list(map(int, sys.stdin.readline().strip().split()))
B = list(map(int, sys.stdin.readline().strip().split()))
CA = Counter(A)
CB = Counter(B)
cnt = 0

for i in A:
    if CB[i] == 0:
        cnt += 1
for i in B:
    if CA[i] == 0:
        cnt += 1
print(cnt)
