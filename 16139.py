import sys

S = sys.stdin.readline().strip()
q = int(sys.stdin.readline())
arr = list()
for _ in range(q):
    arr.append(list(sys.stdin.readline().strip().split()))

abc = []

for i in range(26):
    alp = chr(i+97)
    total = 0
    temp_arr = [0]
    for i in S:
        if i == alp:
            total += 1
            temp_arr.append(total)
        else:
            temp_arr.append(total)
    abc.append(temp_arr)

for a,b,c in arr:
    print(abc[ord(a)-97][int(c)+1]-abc[ord(a)-97][int(b)])

