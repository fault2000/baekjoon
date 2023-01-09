import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    cloth = dict()
    n = int(input())
    total = 1
    for _ in range(n):
        _, m = input().strip().split()
        if m not in cloth:
            cloth[m] = 1
        else:
            cloth[m] += 1
    for v in cloth.values():
        total *= (v+1)
    print(total-1)