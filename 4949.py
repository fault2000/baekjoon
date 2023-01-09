import sys, re

def checkVPS(line):
    arr = []

    for i in line:
        if i == "(":
            arr.append(i)
        elif i == ")":
            if len(arr) == 0:
                return False
            else:
                if arr.pop() != "(":
                    return False
        elif i == "[":
            arr.append(i)
        elif i == "]":
            if len(arr) == 0:
                return False
            else:
                if arr.pop() != "[":
                    return False
    
    if len(arr) != 0:
        return False
    else:
        return True

while True:
    line = sys.stdin.readline()
    temp = ""
    if line == ".\n":
        break
    else:
        for i in line:
            if i == ".":
                break
            temp += i
    temp = re.sub(r'[^\(\)\[\]]', '', line)
    if checkVPS(temp):
        print("yes")
    else:
        print("no")
    
