# tee ratkaisu tänne

def lisaa_opiskelija(rekisteri,nimi):

    if str(nimi) not in rekisteri:
        rekisteri[nimi] = []

def lisaa_suoritus(rekisteri,nimi,suoritus):
    lisataan= True

    if str(nimi) in rekisteri and suoritus[1]>0:
        if rekisteri[nimi] !=[]:
            for i in range (0,len(rekisteri[nimi])):
                if rekisteri[nimi][i][0] == suoritus[0]:
                    if rekisteri[nimi][i][1]<suoritus[1]:
                        rekisteri[nimi].pop(i)
                    else:
                        lisataan=False
            if lisataan==True:
                rekisteri[nimi].append(suoritus)
                
        else:
            rekisteri[nimi].append(suoritus)

def tulosta(rekisteri, nimi):

    if str(nimi) not in rekisteri:
        print(f"ei löytynyt ketään nimellä {nimi}")
    else:    
        print(f"{nimi}:")

        if rekisteri[nimi]==[]:
            print(f" ei suorituksia")
        else:
            summa=0
            kursseja=len(rekisteri[nimi])
            print(f" suorituksia {kursseja} kurssilta:")
            for arvo in rekisteri[nimi]:
                print(f"  {arvo[0]} {arvo[1]}")
                summa=summa+arvo[1]
            print(f" keskiarvo {summa/kursseja}")

def kooste(rekisteri):

    s_arvo=0
    s_nimi=""
    ka_arvo=0
    ka_nimi=""

    for henkilo in rekisteri:

        if len(rekisteri[henkilo])>s_arvo:
            s_arvo=len(rekisteri[henkilo])
            s_nimi=henkilo
        
        lkm=0
        summa=0
        for arvo in rekisteri[henkilo]:
            summa=summa+arvo[1]
            lkm +=1
        
        if summa/lkm > ka_arvo:
            ka_arvo=summa/lkm
            ka_nimi=henkilo
        

    print(f"opiskelijoita {len(rekisteri)}")
    print(f"eniten suorituksia {s_arvo} {s_nimi}")
    print(f"paras keskiarvo {ka_arvo} {ka_nimi}")

if __name__ == "__main__":   
    #Part 1:
    # opiskelijat = {}
    # lisaa_opiskelija(opiskelijat, "Pekka")
    # lisaa_opiskelija(opiskelijat, "Liisa")
    # tulosta(opiskelijat, "Pekka")
    # tulosta(opiskelijat, "Liisa")
    # tulosta(opiskelijat, "Jukka")

    #Part2:
    # opiskelijat = {}
    # lisaa_opiskelija(opiskelijat, "Pekka")
    # lisaa_opiskelija(opiskelijat, "Liisa")
    # lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 3))
    # lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 2))
    # lisaa_suoritus(opiskelijat, "Liisa", ("Tira", 2))
    # tulosta(opiskelijat, "Pekka")

    #Part3:
    # opiskelijat = {}
    # lisaa_opiskelija(opiskelijat, "Pekka")
    # lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 3))
    # lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 2))
    # lisaa_suoritus(opiskelijat, "Pekka", ("Lama", 0))
    # lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 2))
    # tulosta(opiskelijat, "Pekka")

    #Part4:
    # opiskelijat = {}
    # lisaa_opiskelija(opiskelijat, "Pekka")
    # lisaa_opiskelija(opiskelijat, "Liisa")
    # lisaa_suoritus(opiskelijat, "Pekka", ("Lama", 1))
    # lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 1))
    # lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 1))
    # lisaa_suoritus(opiskelijat, "Liisa", ("Ohpe", 5))
    # lisaa_suoritus(opiskelijat, "Liisa", ("Jtkt", 4))
    # kooste(opiskelijat)

    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "pekka")
    lisaa_suoritus(opiskelijat, "pekka", ("ohpe", 1))
    lisaa_suoritus(opiskelijat, "pekka", ("ohpe", 5))
    tulosta(opiskelijat, "pekka")