from collections import Counter
import sys

N = int(input())
x = list()
for _ in range(N):
    x.append(int(sys.stdin.readline()))

print(round(sum(x)/N))

x.sort()
print(x[int(N/2)])

if N == 1:
    print(x[0])
    print(0)
else:
    y = Counter(x).most_common()
    if y[0][1] == y[1][1]:
        print(y[1][0])
    else:
        print(y[0][0])
    print(x[-1]-x[0])