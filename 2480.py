import sys

a, b, c = map(int, sys.stdin.readline().strip().split(" "))

if a==b==c:
    print(10000+a*1000)
elif a==b or b==c:
    print(1000+b*100)
elif c==a:
    print(1000+a*100)
else:
    print(max(a,b,c)*100)
