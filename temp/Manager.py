import os

btns = []
btns.append("Calculator")
btns.append("C")

def isDecimal(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

def isInteger(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def isValidNumber(n):
    n = n.split(".")
    if (len(n) > 2):
        return False
    for i in n:
        if not isInteger(i):
            return False
    return True

def inputNum():
    num = str(input("Enter number:"))
    while (not isValidNumber(num)):
        num = input("Invalid number, try again: ")
    return num

def identifyDevice():
    print (os.system("adb devices"))