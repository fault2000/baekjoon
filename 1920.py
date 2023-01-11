N = int(input())
arrN = list(map(int, input().strip().split()))
arrN.sort()
M = int(input())
arrM = list(map(int, input().strip().split()))

def find(a, b, N):
    start = 0
    end = N
    if N == 1 and a[N//2] != b:
        return 0
    elif a[N//2] == b:
        return 1
    if a[N//2] > b:
        return find(a[:N//2], b, N//2)
    elif a[N//2] < b:
        return find(a[N//2:], b, len(a[N//2:]))
    
for i in arrM:
    print(find(arrN, i, N))