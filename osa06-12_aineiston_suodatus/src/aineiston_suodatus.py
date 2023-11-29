# tee ratkaisu tänne

def suodata_laskut():
    taulukko=[]
    vaarin=[]
    oikein=[]

    
    with open("laskut.csv", "r") as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            sisalto=rivi.split(";")
            lasku=[]

            if "+" in sisalto[1]:
                lasku=sisalto[1].split("+")
                lasku=int(lasku[0])+int(lasku[1])
            else:
                lasku=sisalto[1].split("-")
                lasku=int(lasku[0])-int(lasku[1])

            if lasku==int(sisalto[2]):
                oikein.append(sisalto)
            else:
                vaarin.append(sisalto)

    kirjoita_tiedostoon("oikeat.csv",oikein)
    kirjoita_tiedostoon("vaarat.csv",vaarin)

def kirjoita_tiedostoon(tiedosto:str,sisalto:list):

    with  open(tiedosto, "w") as tiedosto:
        for rivi in sisalto:
            tiedosto.write(f"{str(rivi[0])};{str(rivi[1])};{str(rivi[2])} \n")


if __name__ == "__main__":
    suodata_laskut()