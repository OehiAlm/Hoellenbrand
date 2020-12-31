operator_tuple = ("+", "-", "*", "/")
num1 = int()
num2 = int()
oper1 = str()
repeat = True

def read_first_input():
    global num1
    num1 = input("Enter first number: ")
    if not num1.isalnum():
        print("Not a valid number")
        read_first_input()

def read_second_input():
    global num2
    num2 = input("Enter second number: ")
    if not num2.isalnum():
        print("Not a valid number")
        read_second_input()

def read_operator():
    global oper1
    oper1 = input("Enter operator: ")
    if any((operator in operator_tuple for operator in oper1)):
        str(oper1)
    else:
        print("Operator not recognized. Valid operators are + - * /")
        read_operator()

def read():
    global repeat
    repeat = False
    read_first_input()
    read_operator()
    read_second_input()
    calculate()

def calculate():
    global oper1
    global num1
    global num2
    num1 = int(num1)
    num2 = int(num2)

    if oper1 == "+":
        print("{0} + {1} = {2}".format(num1,num2,num1+num2))
    elif oper1 == "-":
        print("{0} - {1} = {2}".format(num1,num2,num1-num2))
    elif oper1 == "/":
        print("{0} / {1} = {2}".format(num1,num2,num1/num2))
    elif oper1 == "*":
        print("{0} * {1} = {2}".format(num1,num2,num1*num2))
    else:
        print("Something is error. What is it? I don't know. This should never happen.")

def repeating():
    global repeat
    answer = input("Would you like to do it again? (Type 'y' for yes or 'n' for no) ")
    if answer == "y":
        repeat = True
    elif answer == "n":
        repeat = False
        print("Thank you for using Deutsche Bahn")
    else:
        print("What did you just say to me?")
        repeating()

while repeat:
    read()
    repeating()

"""
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
"""

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
