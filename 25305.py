N, k = map(int, input().split())
x = list(map(int, input().split()))

x.sort()
for i in range(k-1):
    x.pop()

print(x[-1])
