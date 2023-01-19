N = int(input())
arrN = list(map(int, input().strip().split()))
arrN.sort()
M = int(input())
arrM = list(map(int, input().strip().split()))

def find(b, start, end):
    global arrN
    if end-start == 1 and arrN[(end-start)//2+start] != b:
        return 0
    elif arrN[(end-start)//2+start] == b:
        return 1
    elif arrN[((end-start)//2+start)] > b:
        return find(b, start, (end-start)//2+start)
    elif arrN[((end-start)//2+start)] < b:
        return find(b, (end-start)//2+start, end)
    
for i in arrM:
    print(find(i, 0, N))