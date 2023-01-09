N = int(input())

arr = [0 for _ in range(N)]
cnt = 0

def check(a):
    for i in range(a):
        if arr[a] == arr[i] or abs(arr[i] - arr[a]) == abs(i - a):
            return False
    return True

def NQueen(a):
    global cnt
    if a == N:
        cnt += 1
        return
    
    for i in range(N):
        arr[a] = i
        if check(a):
            NQueen(a+1)

NQueen(0)

print(cnt)