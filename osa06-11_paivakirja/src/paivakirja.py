# tee ratkaisu tänne

def lue_tiedosto():
    
    with open("paivakirja.txt", "r") as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            sisalto=rivi.split(",")

            print(sisalto[0])

def kirjoita_tiedostoon():
    merkinta=input("Anna merkintä:")

    with  open("paivakirja.txt", "a") as tiedosto:
        tiedosto.write(merkinta + "\n")
    print("Päiväkirja tallennettu")





print("1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta")

while(True):
    valinta=int(input("Valinta:"))

    if valinta==1:
        print(valinta)
        kirjoita_tiedostoon()
    elif valinta==2:
        lue_tiedosto()
    elif valinta==0:
        print("Heippa!")
        break