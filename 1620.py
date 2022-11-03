import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().strip().split(" "))
arr = []

for i in range(N):
    arr.append([i, sys.stdin.readline().strip()])

arr2 = Counter(arr).get("Bulbasaur")

