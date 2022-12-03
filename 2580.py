import sys

sudoku = []
zero = []

for _ in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zero.append([i, j])

def rowCheck(x, i):
    for j in range(9):
        if sudoku[i][j] == x:
            return False
        return True

def columnCheck(x, j):
    for i in range(9):
        if sudoku[i][j] == x:
            return False
    return True

def squareCheck(x, a, b):
    for i in range((a+1)//3*3):
        for j in range((b+1)//3*3):
            if x == sudoku[i][j]:
                return False
    return True

while len(zero)==0:
    for i in range(9):
        