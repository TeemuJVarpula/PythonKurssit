# tee ratkaisu tänne
from random import sample

def heita(noppa:str):
    A =[3, 3, 3, 3, 3, 6]
    B =[2, 2, 2, 5, 5, 5]
    C =[1, 4, 4, 4, 4, 4]

    nopat={"A":A,"B":B,"C":C}

    tulos=sample(nopat[noppa],1)
    
    return tulos[0]

def pelaa(noppa1: str, noppa2: str, kertaa: int):

    avoitot=0
    bvoitot=0
    tasat=0

    for i in range (0,kertaa):
        a=heita(noppa1)
        b=heita(noppa2)
        print(f"{a},{b}")
        if a>b:
            avoitot +=1
        elif b>a:
            bvoitot +=1
        else:
            tasat +=1
        
    return (avoitot,bvoitot,tasat)
    
if __name__ == "__main__":

    # tulos = pelaa("A", "C", 1000)
    # print(tulos)
    tulos = pelaa("B", "B", 1000)
    print(tulos)