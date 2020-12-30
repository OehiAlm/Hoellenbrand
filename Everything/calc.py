
def read():
    global num1
    num1 = input("Enter first number: ")
    try:
        int(num1)
    except ValueError:
        print("Not a valid number")
        read()

    global oper1
    oper1 = input("Enter operator: ")
    if any((operator in operator_tuple for operator in oper1)):
        str(oper1)
    else:
        print("Operator not recognized. Valid operators are + - * /")
        read()

    global num2
    num2 = input("Enter second number: ")
    try:
        int(num2)
    except ValueError:
        print("Not a valid number")
        read()


operator_tuple = ("+", "-", "*", "/")
num1 = int()
num2 = int()
oper1 = str()

read()

"""
try:
    int(num1)
except ValueError:
    try:
        int(num2)
    except ValueError:
        print("Number 1 and 2 are invalid")
        read()

try:
    int(num1)
except ValueError:
    print("Number 1 is invalid")
    read()

try:
    int(num2)
except ValueError:
    print("Number 2 is invalid")
    read()

    #print("Number 1 is invalid")
    #read()
"""

#if not num1.isdigit() or not num2.isdigit():
#    print("Please input valid numbers")
#    restart()

num1 = int(num1)
num2 = int(num2)

if oper1 == "+":
    print(num1 + num2)
elif oper1 == "-":
    print(num1 - num2)
elif oper1 == "/":
    print(num1 / num2)
elif oper1 == "*":
    print(num1 * num2)
else:
    print("Operator not recognized. Valid operators are + - * /")
    read()
