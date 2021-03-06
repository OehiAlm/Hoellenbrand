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

    #print(find(9,[3,5,5,2,6]))

# Write a method that takes an unsigned integer as input and returns true if all the digits in the base
# 10 representation of that number are unique.
# bool AllDigitsUnique(unsigned int value)
#Example:
#AllDigitsUnique(48778584) returns false
#AllDigitsUnique(17308459) returns true
def Uniqueness_Check (integer):

    unique = False
    zahl = str(integer)
    count = (len(zahl))
    sat = set()

    for x in range(count):
        sat.add(zahl[x])

    if len(sat) == count:
        unique = True

    print(zahl + " = hat {} Ziffern".format(count))
    print(zahl + " = hat {} Einträge".format(len(sat)))
    print(sat)

    return unique

    #print(Uniqueness_Check(48778584))
    #print(Uniqueness_Check(17308459))


def is_anagram (str1, str2):
    Anagramme = [["Altersvorsorge", "sorgloser Vater"], ["Ablasshandel", "Hassballaden"],
                 ["alternative Energien", "verratene Genitalien"], ["Tom", "Lukas"]]
    sortiert1 = ''.join(sorted(str1.lower())).replace(" ","")
    print(sortiert1)

    sortiert2 = ''.join(sorted(str2.lower())).replace(" ","")
    print(sortiert2)

    if sortiert1 == sortiert2:
        return True
    else:
        return False

    #print(is_anagram(Anagramme[3][0],Anagramme[3][1]))

# Given a 3x3 matrix of a completed tic-tac-toe game, create a function that returns whether the game is a win for "X", "O", or a "Draw",
# where "X" and "O" represent themselves on the matrix, and "E" represents an empty spot.

# Examples
Game_1 = [
  ["X", "O", "X"],      # X, 0, 0
  ["O", "X",  "O"],     # 0, X, X
  ["O", "X",  "X"]      # X, 0, X
] # ➞ "X"

Game_2 = [
  ["O", "O", "O"],
  ["O", "X", "X"],
  ["E", "X", "X"]
] # ➞ "O"

Game_3 = [
  ["X", "X", "O"],
  ["O", "O", "X"],
  ["X", "X", "O"]
] # ➞ "Draw"


def Who_won (stuff):
    Winner = "Undecided"

    for t in matrix:
        #print(t)

        if t[0] == t[1] and t[0] == t[2]:
            Winner = t[0]
            print("Drei Gleiche!! yaaaay")
        else:
            print("kein Wiener")

    for t in matrix_rotated:
        #print(t)

        if t[0] == t[1] and t[0] == t[2]:
            Winner = t[0]
            print("Drei Gleiche!! yaaaay")
        else:
            print("kein Wiener")

    if (matrix[0][0] == matrix[1][1] and matrix[0][0] == matrix[2][2]) or \
       (matrix[2][0] == matrix[1][1] and matrix[2][0] == matrix[0][2]):
        Winner = matrix[1][1]
        print("Drei Gleiche!! yaaaay")
    else:
        print("kein Wiener")

    print("\nGesamtgewinner = "+ Winner + "\n")

Who_won(Game_1)
Who_won(Game_2)
Who_won(Game_3)
Who_won(Game_4)