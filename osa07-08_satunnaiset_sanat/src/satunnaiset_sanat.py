# tee ratkaisu tänne
from random import sample

def sanat(n: int, alku: str):
    sanat=[]
    valitut=[]

    with open("sanat.txt") as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")

            if rivi.startswith(alku):
                sanat.append(rivi)

    valitut=sample(sanat,n)

    return valitut




if __name__ == "__main__":
    
    lista = sanat(3, "ca")
    for sana in lista:
        print(sana)
 