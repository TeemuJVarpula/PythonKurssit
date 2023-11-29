# tee ratkaisu tänne
def lue_tiedosto():
    with open("matriisi.txt") as tiedosto:
        taulukko=[]
        rivilaskuri=0

        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            sisalto=rivi.split(",")
            
            taulukko.append([])

            for luku in sisalto:
                taulukko[rivilaskuri].append(luku)
            
            rivilaskuri +=1

        return taulukko
    
def summa():
    matriisi=lue_tiedosto()
    summa=0

    for rivi in matriisi:
        for luku in rivi:
            summa= summa + int(luku)
    
    return summa


    
def maksimi():
    matriisi=lue_tiedosto()
    suurin=0

    for rivi in matriisi:
        for luku in rivi:
            if suurin < int(luku):
                suurin=int(luku)
        

    return suurin

def rivisummat():
    matriisi=lue_tiedosto()
    summalista=[]

    for rivi in range (0,len(matriisi)):
        summalista.append(0)
        for luku in matriisi[rivi]:
            summalista[rivi]=summalista[rivi]+int(luku)

    return summalista

if __name__ == "__main__":

    print(lue_tiedosto())
    print(summa())
    print(rivisummat())
    print(maksimi())