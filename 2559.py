import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
new_arr = [0]
total = 0
answer_arr = list()

for i in arr:
    total += i
    new_arr.append(total)

for i in range(N-K+1):
    answer_arr.append(new_arr[i+K]-new_arr[i])

print(max(answer_arr))