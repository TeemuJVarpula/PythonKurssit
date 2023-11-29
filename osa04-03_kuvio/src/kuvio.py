# kopioi edellisestä tehtävästä funktion viiva koodi tänne, ja toteuta funktio kuvio sitä hyödyntäen
def viiva(pituus,merkki):
    mjono=""
    for i in range(0,pituus):
        if len(merkki)==0:
            mjono=mjono + "*"
        else:
            mjono = mjono + merkki[0]
    
    print(mjono)

def kuvio(koko,kuvio,koko2,kuvio2):
    laskuri = koko-1

    for i in range(0,koko):
        viiva(koko-laskuri, kuvio)
        laskuri -=1

    for i in range(0,koko2):
        viiva(koko, kuvio2)

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kuvio(5, "X", 3, "*")
    print()
    kuvio(2, "o", 4, "+")
    print()
    kuvio(3, ".", 0, ",")
