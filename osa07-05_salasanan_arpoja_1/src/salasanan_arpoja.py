# tee ratkaisu tänne
from string import ascii_letters
from random import sample

def luo_salasana(maara: int):
    kirjaimet=[]
    numerot=[]
    valittu=""

    for kirjain in ascii_letters:
        kirjaimet.append(kirjain)
        if kirjain=='z':
            break

    numerot = sample(list(range(0, len(kirjaimet))), maara)

    for numero in numerot:
        valittu= valittu+(kirjaimet[numero])
    
    return valittu

if __name__ == "__main__":
    
    for i in range(10):
        print(luo_salasana(8))