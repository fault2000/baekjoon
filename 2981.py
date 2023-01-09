# import sys

# def abc(a, b): # a, b의 최대공약수 구하기
#     if b == 0:
#         return a
#     return abc(b, a%b)

# def abcd(a): # a의 모든 약수 구하기
#     b = int(a**(1/2))
#     output = set()
#     for i in range(2, b+1):
#         if b%i==0:
#             output.add(i)
#             output.add(int(a/i))
#     output.add(a)
#     return output

# N = int(sys.stdin.readline())
# arr = list()

# for _ in range(N):
#     arr.append(int(sys.stdin.readline()))
    
# arr.sort()
# a = arr[1] - arr[0]
# for i in range(2, len(arr)):
#     if a>arr[i]-arr[i-1]:
#         a = abc(a, arr[i]-arr[i-1])
#     else:
#         a = abc(arr[i]-arr[i-1], a)

# output = abcd(a)
# print(*sorted(list(output)))

N = int(input())
num = sorted([int(input()) for _ in range(N)])
re_num = []

for i in range(1, N):
    re_num.append(num[i] - num[i-1])

def findGCD(a, b):
    num = b
    div = a
    rest = num % div
    while rest != 0:
        num = div
        div = rest
        rest = num % div
    return div

GCD = re_num[0]
for idx in range(1, len(re_num)):
    GCD = findGCD(GCD, re_num[idx])

result = set()
for i in range(2, int(GCD**0.5) + 1):
    if GCD % i == 0:
        result.add(i)
        result.add(GCD // i)
result.add(GCD)
print(*sorted(list(result)))