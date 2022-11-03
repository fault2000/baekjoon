import sys
from collections import Counter

N = int(sys.stdin.readline())
arr = map(int, sys.stdin.readline().split(" "))
v = int(sys.stdin.readline())

arr2 = Counter(arr).most_common()

for i in arr2:
    if int(i[0]) == v:
        print(i[1])
        exit()
print(0)


