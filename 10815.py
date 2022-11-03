import sys
from collections import Counter

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split(" ")))
M = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().strip().split(" ")))

arr3 = Counter(arr)
for i in arr2:
    if arr3.get(i) is None:
        print("0", end=" ")
    else:
        print("1", end=" ")

