import random
import os
import timeit

# Wichtelprogramm
start = timeit.default_timer()

Beyssells = ["Stefan", "Ute", "Lena", "Wiebke", "Caro"]
Piepers = ["Joerg", "Elke", "Lukas", "Jana", "Tom", "Anna"]
Sommers = ["Peter", "Katrin", "Scherin", "Christian", "Anne", "Alex"]

Falkis = ["Guenter", "Susanne", "Tim", "Jasmin", "Robin", "Marla", "Kevin", "Ute", "Doris", "Frauke", "Falk", "Trinh"]

OGs = ["Guenter", "Susanne"]
Millenials = ["Tim", "Jasmin"]
NewlyWedds = ["Marla", "Kevin"]
Cuties = ["Falk", "Trinh"]
Rest1 = ["Robin"]
Rest2 = ["Ute"]
Rest3 = ["Doris"]
Rest4 = ["Jen"]


Nachname_O = " OGs"
Nachname_M = " Millenials"
Nachname_N = " NewlyWedds"
Nachname_C = " Cuties"
Nachname_R1 = " Rest1"
Nachname_R2 = " Rest2"
Nachname_R3 = " Rest3"
Nachname_R4 = " Rest4"
OGs = [Vorname + Nachname_O for Vorname in OGs]
Millenials = [Vorname + Nachname_M for Vorname in Millenials]
NewlyWedds = [Vorname + Nachname_N for Vorname in NewlyWedds]
Cuties = [Vorname + Nachname_C for Vorname in Cuties]
Rest1 = [Vorname + Nachname_R1 for Vorname in Rest1]
Rest2 = [Vorname + Nachname_R2 for Vorname in Rest2]
Rest3 = [Vorname + Nachname_R3 for Vorname in Rest3]
Rest4 = [Vorname + Nachname_R4 for Vorname in Rest4]

Namen = OGs + Millenials + NewlyWedds + Cuties + Rest1 + Rest2 + Rest3 + Rest4
Kombinations_Counter = 0

#region Hier werden Ordner angelegt und Textdateien gebaut, etc.
def Textersteller (Name_des_Schenkers, Name_des_Beschenkten):
    f = open("Wichteltexte_v2/"+Name_des_Schenkers+".txt", "w")
    f.write("Hallo "+Name_des_Schenkers+"! \nDu musst "+Name_des_Beschenkten+" beschenken."
    "\nInflationsbedingt liegen wir dieses Jahr bei 50-60 Euro.\nLass dir was einfallen und viel Spass!")
    f.close()

if not os.path.isdir("../Everything/Wichteltexte_v2/"):
    os.mkdir("Wichteltexte_v2")

dir_name = "../Everything/Wichteltexte_v2/"
Textordner = os.listdir(dir_name)

for item in Textordner:
    if item.endswith(".txt"):
        os.remove(os.path.join(dir_name, item))

# os.remove("Wichteltexte/")
#endregion

print("Dabei sind " + str(len(Namen)) + " Personen")

Schenker = Namen.copy()
Beschenkte = Namen.copy()

#print(Schenker)
#print(Beschenkte)

# Voraussetzung, dass die Liste noch nicht leer ist, damit wir weiter machen
while len(Schenker) >= 1:
    aktueller_Schenker = random.choice(Schenker)
    aktuell_Beschenkter = random.choice(Beschenkte)

    aktueller_Schenker_Nachname = aktueller_Schenker.partition(" ")[2]
    aktueller_Beschenkter_Nachname = aktuell_Beschenkter.partition(" ")[2]

    #print("aktuell Beschenker Nachname = " + aktueller_Beschenkter_Nachname)
    #print("Schenker Nachname = " + aktueller_Schenker_Nachname)

    while aktueller_Beschenkter_Nachname == aktueller_Schenker_Nachname:
        print(aktueller_Schenker + " darf nicht " + aktuell_Beschenkter + " beschenken! Neue Kombination wird gesucht")
        aktueller_Schenker = random.choice(Schenker)
        aktuell_Beschenkter = random.choice(Beschenkte)
        Kombinations_Counter = Kombinations_Counter + 1
        aktueller_Schenker_Nachname = aktueller_Schenker.partition(" ")[2]
        aktueller_Beschenkter_Nachname = aktuell_Beschenkter.partition(" ")[2]

        if len(Schenker) == 1:
            print("\n Wir müssen alles von vorne machen!!!! \n")
            Schenker = Namen.copy()
            Beschenkte = Namen.copy()

    #print("habe zwei unterschiedliche Nachnamen gefunden")
    print(aktueller_Schenker + " beschenkt " + aktuell_Beschenkter)
    Textersteller(aktueller_Schenker,aktuell_Beschenkter)
    Schenker.remove(aktueller_Schenker)
    Beschenkte.remove(aktuell_Beschenkter)

stop = timeit.default_timer()
print("Time: ", (stop - start)*1000, " Millisekunden hats gebraucht")
print("Es hat ", Kombinations_Counter, "überflüssige Kombinationsversuche gebraucht")