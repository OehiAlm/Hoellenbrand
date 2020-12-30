print("Gib mir 3 Zahlen")
num1 = input("erste Zahl: ")
num2 = input("zweite Zahl: ")
num3 = input("dritte Zahl: ")

input("Danke, Enter um weiter zu machen...")
number_list = [int(num1), int(num2), int(num3)]

original_tup = tuple(number_list)

print("Deine Liste: " + str(number_list))
number_list.sort()
print("Sortierte Liste: " + str(number_list))
print("Summe der Liste: " + str(sum(number_list)))


print("Gib mir nochmal 3 Zahlen")
num4 = input("vierte Zahl: ")
num5 = input("fuenfte Zahl: ")
num6 = input("sechste Zahl: ")

secondnumber_list = [int(num4), int(num5), int(num6)]
number_list = list(original_tup)

number_list.extend(secondnumber_list)
input("Danke, Enter um weiter zu machen...")
print("Beide Listen kombiniert (unsortiert): " + str(number_list))
number_list.sort()
print("Summe der neuen Liste: " + str(sum(number_list)))
print("Sortierte neue Liste: " + str(number_list))
print("Origianl Liste 1: " + str(list(original_tup)))
print("Original Liste 2: " + str(secondnumber_list))
