# tee ratkaisu tänne
def syotaTietoa():
    tiedot=[]

    while True:
        rivi=input("Koepisteet ja harjoitusten määrä: ")
        #print(rivi)
        if rivi=="":
            break
        else:
            tiedot.append(rivi.split());
            #print(tiedot)
    #print(f"Tiedot {tiedot}")
    return tiedot

def laskeArvosanat(lista1):

    arvosanat=[]
    pisteet=[]
    tulos=0

    for lukemat in lista1:
        pisteet.append([lukemat[0],f"{(int(lukemat[1])-4.5)/10:0.0f}"])

    for lukemat2 in pisteet:
        tulos=int(lukemat2[0])+int(lukemat2[1])
        
        if int(lukemat2[0])<10:
            arvosanat.append([0,tulos])
        elif tulos>=28:
            arvosanat.append([5,tulos])
        elif tulos>=24:
            arvosanat.append([4,tulos])
        elif tulos>=21:
            arvosanat.append([3,tulos])
        elif tulos>=18:
            arvosanat.append([2,tulos])
        elif tulos>=15:
            arvosanat.append([1,tulos])
        else:
            arvosanat.append([0,tulos])
    #print(f"arvosanat {arvosanat}")
    return arvosanat



def keskiarvo(lasketut1):
    summa=0
    lkm=0

    for arvo in lasketut1:
        lkm +=1
        summa=int(summa + int(arvo[1]))

    return f"{(summa/lkm):0.1f}"


def hprosentti(lasketut2):
    
    summa=0
    lkm=0

    for lukemat in lasketut2:
        if lukemat[0]>0:
            summa +=1
        
        lkm +=1
       # print(f"hprosentti {lukemat[0]} {summa} {lkm}")

    return f"{((summa/lkm)*100):0.1f}"



def tulosta_jakauma(lasketut3):

    jakauma=[0,0,0,0,0,0]

    for lukema in lasketut3:
        jakauma[lukema[0]] +=1

    print(f"Arvosanajakauma:")
    for i in range(5,-1,-1):
        teksti=""
        for j in range (0,jakauma[i]):
            teksti = teksti + "*"

        print(f"{i}: {teksti}")




def main():
    ka=0.0
    hp=0
    lasketut=[]
    4
    lista= syotaTietoa()

    lasketut=laskeArvosanat(lista)

    print("Tilasto:")
    ka= keskiarvo(lasketut)
    print(f"Pisteiden keskiarvo: {ka}")
    
    hp= hprosentti(lasketut)
    print(f"Hyväksymisprosentti: {hp}")
    tulosta_jakauma(lasketut)


main()