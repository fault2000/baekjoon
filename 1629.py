A, B, C = map(int, input().strip().split())

def multiply(A, B, C):
    if B == 1:
        return A % C
    elif B % 2 == 0:
        return multiply(A, B//2, C)**2%C
    else:
        return multiply(A, B//2, C)**2*A%C

print(multiply(A, B, C))