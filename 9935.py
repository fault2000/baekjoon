str = input().strip()
exp = input().strip()
expLen = len(exp)
expArr = []
for i in exp:
    expArr.append(i)
arr = []

def check(arr, expArr, expLen):
    if len(arr) >= expLen:
        if arr[-expLen:] == expArr:
            for _ in range(expLen):
                arr.pop()
            check(arr, expArr, expLen)

for i in range(len(str)):
    arr.append(str[i])
    check(arr, expArr, expLen)

if len(arr) == 0:
    print("FRULA")
else:
    ans = ""
    for i in arr:
        ans += i
    print(ans)