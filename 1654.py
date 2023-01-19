import sys

K, N = map(int, sys.stdin.readline().strip().split())
arr = []
for _ in range(K):
    arr.append(int(sys.stdin.readline()))
arr.sort()
mid = min(2**31, arr[0])

def lan(cut):
    global arr, N
    total = 0
    for i in arr:
        total += i//cut
    if total == N:
        
    elif total > N:
        return lan(cut*2)
    elif total < N:
        return lan(cut//2)