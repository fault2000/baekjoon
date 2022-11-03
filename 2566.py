import sys

max = 0
maxi = 1
maxj = 1
for i in range(9):
    A = sys.stdin.readline().strip().split(" ")
    for j in range(9):
        if int(A[j]) > int(max):
            max = A[j]
            maxi = i+1
            maxj = j+1

print(max)
print(maxi, maxj)
