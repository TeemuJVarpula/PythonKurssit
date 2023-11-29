# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(pituus,merkki):
    mjono=""
    for i in range(0,pituus):
        if len(merkki)==0:
            mjono=mjono + "*"
        else:
            mjono = mjono + merkki[0]
    
    print(mjono)

def kolmio(koko):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    laskuri = koko-1

    for i in range(0,koko):
        viiva(koko-laskuri, "#")
        laskuri -=1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kolmio(5)

