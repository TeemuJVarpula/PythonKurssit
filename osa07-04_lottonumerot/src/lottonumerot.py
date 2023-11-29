# tee ratkaisu tänne
from random import sample

def lottonumerot(maara: int, alaraja: int, ylaraja: int):
    numerot=[]
    numerot = sample(list(range(alaraja, ylaraja)), maara)
    numerot.sort()

    return numerot

if __name__ == "__main__":
    
    for numero in lottonumerot(7, 1, 40):
        print(numero)