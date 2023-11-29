# tee ratkaisu tänne

def lue_tiedosto():
    with open("wordlist.txt") as tiedosto:
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



