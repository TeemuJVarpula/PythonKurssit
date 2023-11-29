# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(pituus,merkki):
    mjono=""
    for i in range(0,pituus):
        if len(merkki)==0:
            mjono=mjono + "*"
        else:
            mjono = mjono + merkki[0]
    
    print(mjono)

def risulaatikko(korkeus):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    for i in range(0,korkeus):
        viiva(10, "#")

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risulaatikko(5)
