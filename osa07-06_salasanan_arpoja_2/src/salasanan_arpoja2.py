# tee ratkaisu tänne
from string import ascii_letters
from random import randint

def luo_hyva_salasana(maara: int,numero: bool, merkki: bool):
    valittavat=[]
    numerot=["0","1","2","3","4","5","6","7","8","9"]
    merkit=["!","?","=","+","-","(",")","#",]
    valittu=""
    loydyttava=[1,0,0]

    for kirjain in ascii_letters:
        valittavat.append(kirjain)
        if kirjain=='z':
            break
    
    if numero==True:
        for nro in range (0,len(numerot)):
            valittavat.append(str(nro))
        loydyttava[1]=1

    if merkki==True:
        for nro2 in range (0,len(merkit)):
            valittavat.append(merkit[nro2])
        loydyttava[2]=1

    while loydyttava!=[0,0,0]:
        etsityt=loydyttava

        for i in range (0,maara):
            valittu=valittu+str(valittavat[randint(0,len(valittavat)-1)])

        for j in valittu:
            if j in ascii_letters:
                etsityt[0]=0
            
            if numero==True and str(j) in numerot:
                etsityt[1]=0
            
            if merkki==True and j in merkit:
                etsityt[2]=0

        if etsityt!=[0,0,0]:
            valittu=""
    
    return valittu

if __name__ == "__main__":
    
    for i in range(10):
        print(luo_hyva_salasana(8, True, True))