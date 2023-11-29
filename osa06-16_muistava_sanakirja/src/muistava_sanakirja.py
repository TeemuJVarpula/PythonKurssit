# tee ratkaisu tänne

def hae_sanaa():
    
    sana=input("Anna sana:")

    with open("sanakirja.txt", "r") as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            sisalto=rivi.split(",")
            if sana in rivi:
                print(f"{sisalto[0]} {sisalto[1]} {sisalto[2]}")

def lisaa_sana():
    merkinta=input("Anna sana suomeksi:")
    merkinta2=input("Anna sana englanniksi:")

    with  open("sanakirja.txt", "a") as tiedosto:
        tiedosto.write(f"{merkinta},-,{merkinta2}\n")
    print("Sanapari lisätty")


print("1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu")

while(True):
    valinta=int(input("Valinta:"))

    if valinta==1:
        print(valinta)
        lisaa_sana()
    elif valinta==2:
        hae_sanaa()
    elif valinta==3:
        print("Moi!")
        break