# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(pituus,merkki):
    mjono=""
    for i in range(0,pituus):
        if len(merkki)==0:
            mjono=mjono + "*"
        else:
            mjono = mjono + merkki[0]
    
    print(mjono)

def nelio(koko, merkki):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    for i in range(0,koko):
        viiva(koko, merkki)


# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    nelio(5, "*")
    print()
    nelio(3, "o")