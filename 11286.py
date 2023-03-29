import sys

class heap:
    def heappush(arr, x):
        child = len(arr)-1
        while child != 0:
            parent = (child - 1) // 2
            if arr[]


N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr, abs(x))

