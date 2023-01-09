X = int(input())
global output
output = [0 for _ in range(X-1)]

for i in range(len(output)):
    if X % 3 == 0 and X % 2 == 0:
        output[i]

makeOne(X, 0)
print(min(output))