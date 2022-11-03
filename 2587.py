x = list()
for _ in range(5):
    x.append(int(input()))

total = 0
for i in x:
    total += i

print(int(total/5))

x.sort()

print(x[2])

