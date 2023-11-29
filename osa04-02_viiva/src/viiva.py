# tee ratkaisu tänne

def viiva(pituus,merkki):
    mjono=""
    for i in range(0,pituus):
        if len(merkki)==0:
            mjono=mjono + "*"
        else:
            mjono = mjono + merkki[0]
    
    print(mjono)

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    viiva(7, "%")
    viiva(10, "LOL")
    viiva(3, "")