import random
import os
# Wichtelprogramm

Beyssells = ["Stefan", "Ute", "Lena", "Wiebke", "Caro"]
Piepers = ["Joerg", "Elke", "Lukas", "Jana", "Tom"]
Sommers = ["Peter", "Katrin", "Scherin", "Christian", "Anne", "Alex"]

Namen = Beyssells + Piepers + Sommers

Beyssell_Ziele = Piepers.copy() + Sommers.copy()
Pieper_Ziele = Beyssells.copy() + Sommers.copy()
Sommer_Ziele = Beyssells.copy() + Piepers.copy()

#print("Liste für Beyssells = "+ str(Beyssell_Ziele))
#print("Liste für Piepers = "+ str(Pieper_Ziele))
#print("Liste für Sommers = "+ str(Sommer_Ziele))

def Textersteller (Name_des_Schenkers, Name_des_Beschenkten):
    f = open("Wichteltexte_v2/"+Name_des_Schenkers+".txt", "w")
    f.write("Hallo "+Name_des_Schenkers+"! \nDu musst "+Name_des_Beschenkten+" beschenken."
    "\nInflationsbedingt liegen wir dieses Jahr bei 20-30 Euro.\nLass dir was einfallen und viel Spass!")
    f.close()

if not os.path.isdir("../Everything/Wichteltexte_v2/"):
    os.mkdir("Wichteltexte_v2")

dir_name = "../Everything/Wichteltexte_v2/"
Textordner = os.listdir(dir_name)

for item in Textordner:
    if item.endswith(".txt"):
        os.remove(os.path.join(dir_name, item))

# os.remove("Wichteltexte/")

print("Dabei sind " + str(len(Namen)) + " Personen")

Schenker = Beyssells.copy()
Beschenkte = Piepers.copy() + Sommers.copy()

print(Schenker)
print(Beschenkte)

while len(Schenker) >= 1:
    aktueller_Schenker = random.choice(Schenker)
    aktuell_Beschenkter = random.choice(Beschenkte)

gleiche_Familie = aktueller_Schenker
print(aktueller_Schenker[len(aktueller_Schenker)-1])

while aktuell_Beschenkter == aktueller_Schenker:

        if len(Schenker) == 1:
           print("Ich habe neu gemacht")
           Schenker = Namen.copy()
           Beschenkte = Namen.copy()


        aktueller_Schenker = random.choice(Schenker)
        aktuell_Beschenkter = random.choice(Beschenkte)
        print("Selbst beschenken gildet nicht!")

    #print(aktueller_Schenker + " beschenkt " + aktuell_Beschenkter)
    Textersteller(aktueller_Schenker,aktuell_Beschenkter)
    Schenker.remove(aktueller_Schenker)
    Beschenkte.remove(aktuell_Beschenkter)