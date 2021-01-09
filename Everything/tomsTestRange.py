#Functions #1. Write a Python function to find the Max of three numbers.
def max():
    def find_max2(num1, num2):
        if num1 > num2:
            return num1
        return num2

    def find_max3(num1, num2, num3):
        return find_max2(num1, find_max2(num2, num3))

    print(find_max3(5, 99, -44))


#Functions #2. Write a Python function to multiply all the numbers in a list.
def multi(list):
    print("Wir nehmen kein Set, weil da nur jede Zahl einmal drin vorkommen darf. Else there's nuttin'")

    # list = []
    answer = 1

    for zahl in list:
        print("jetzt ist es grad {}".format(answer))
        print("zahl zum multiplizieren = {}".format(zahl))
        answer *= zahl

    return answer


#Functions #7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters
def uplo(el_texto):
    uber_case_letters_count = 0
    lover_case_letters_count = 0

    for zeichen in el_texto:
        if zeichen.isupper():
            uber_case_letters_count += 1

        elif zeichen.islower():
            lover_case_letters_count += 1

    return uber_case_letters_count, lover_case_letters_count

    # el_inputto = input("please put in a string here: ")
    # print("We have {0[0]} upper case letters, {0[1]} lower case letters".format(uplo(el_inputto)))


#Basic II #16. Write a Python program to get the third side of right angled triangle from two given sides.
def pytha(num1,num2,operation_type = "Hypo"):
    if operation_type == "Hypo":
        hypo = num1**2 + num2**2
        return hypo**0.5
    else:
        if num1 > num2:
            return (num1 ** 2 - num2 ** 2) ** 0.5

        else:
            return (num2 ** 2 - num1 ** 2) ** .5

    #print(pytha(3, 4, "nope"))


#Bisect #4. Write a Python program to find the first occurrence of a given number in a sorted list using Binary Search (bisect).
def find(number, list):
    from bisect import bisect_left

    if number in list:

        list.sort()
        print(list)

        return bisect_left(list, number)
    else:
        return "nono"

print(find(9,[3,5,5,2,6]))


from bisect import bisect_left
def Binary_Search(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1

nums = [1, 2, 3, 4, 8, 8, 10, 12]
x = 8
num_position = Binary_Search(nums, x)
if num_position == -1:
    print(x, "is not present.")
else:
    print("First occurrence of", x, "is present at index", num_position)
