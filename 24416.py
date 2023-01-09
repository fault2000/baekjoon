recursion = 0
dynamic = 0

def fibonacci(n):
    global dynamic
    f = []

    f.append(1)
    f.append(1)
    for i in range(2, n):
        dynamic += 1
        f.append(f[i-1] + f[i-2])
    return f[n-1]

a = int(input())
print(fibonacci(a), a-2)