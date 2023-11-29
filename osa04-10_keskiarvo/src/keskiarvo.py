# tee ratkaisu tänne
def keskiarvo(lista):
    summa=0

    for i in range (0,len(lista)):
        summa=summa+lista[i]

    return summa/len(lista)

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    lista = [1,2,3,4,5] 
    tulos = keskiarvo(lista) 
    print(tulos)
