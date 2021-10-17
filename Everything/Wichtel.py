import random
import os
# Wichtelprogramm

Namen = ["Tom", "Lukas", "Anne", "Christian", "Joerg", "Elke", "Katrin", "Peter", "Stefan", "Ute",
         "Lena", "Wiebke", "Caro", "Jana", "Scherin", "Alex", "Flo", "Felix"]

def Textersteller (Name_des_Schenkers, Name_des_Beschenkten):
    f = open("Wichteltexte/"+Name_des_Schenkers+".txt", "w")
    f.write("Hallo "+Name_des_Schenkers+"! \nDu musst "+Name_des_Beschenkten+" beschenken.\nViel Spass!")
    f.close()

if not os.path.isdir("../Everything/Wichteltexte/"):
    os.mkdir("Wichteltexte")

dir_name = "../Everything/Wichteltexte/"
Textordner = os.listdir(dir_name)

for item in Textordner:
    if item.endswith(".txt"):
        os.remove(os.path.join(dir_name, item))

# os.remove("Wichteltexte/")

print("Dabei sind " + str(len(Namen)) + " Personen")

Schenker = Namen.copy()
Beschenkte = Namen.copy()

# print(Schenker)
# print(Beschenkte)

while len(Schenker) >= 1:
    aktueller_Schenker = random.choice(Schenker)
    aktuell_Beschenkter = random.choice(Beschenkte)

    while aktueller_Schenker == aktuell_Beschenkter:

        if len(Schenker) == 1:
           print("Ich habe neu gemacht")
           Schenker = Namen.copy()
           Beschenkte = Namen.copy()


        aktueller_Schenker = random.choice(Schenker)
        aktuell_Beschenkter = random.choice(Beschenkte)
        print("REDO")

    #print(aktueller_Schenker + " beschenkt " + aktuell_Beschenkter)
    Textersteller(aktueller_Schenker,aktuell_Beschenkter)
    Schenker.remove(aktueller_Schenker)
    Beschenkte.remove(aktuell_Beschenkter)