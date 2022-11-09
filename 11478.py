import sys

S = sys.stdin.readline().strip()

arr = set()

for i in range(1, len(S)+1):
    end = i
    start = 0
    while end <= len(S):
        arr.add(S[start:end])
        end += 1
        start += 1

print(len(arr))