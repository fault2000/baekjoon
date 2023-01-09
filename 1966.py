import collections, sys
T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().strip().split())
    arr = collections.deque(map(int, sys.stdin.readline().strip().split()))
    top = max(arr)
    cnt = 0
    while True:
        if arr[0] == top:
            if M == 0:
                cnt += 1
                break
            else:
                cnt += 1
                arr.popleft()
                top = max(arr)
                M -= 1
        else:
            tmp = arr.popleft()
            arr.append(tmp)
            if M == 0:
                M = len(arr)-1
            else:
                M -= 1
    print(cnt)

    
    
