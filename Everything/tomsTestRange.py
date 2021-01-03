# 1. Write a Python function to find the Max of three numbers.

def find_max2(num1, num2):
    if num1 > num2:
        return num1
    return num2


def find_max3(num1, num2, num3):
    return find_max2(num1, find_max2(num2, num3))


print(find_max3(5, 99, -44))
