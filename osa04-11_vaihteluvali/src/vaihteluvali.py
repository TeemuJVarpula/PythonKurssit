# tee ratkaisu tänne
def vaihteluvali(lista):

    suurin=0
    if lista[0]:
        pienin=int(lista[0])
    else:
        pienin=0

    for i in range (0,len(lista)):
        if suurin < lista[i]:
            suurin=lista[i]
        
        if pienin > lista[i]:
            pienin = lista[i]

    if suurin==pienin:
        return 0
    else:
        return suurin-pienin

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    lista = [1,2,3,4,5] 
    tulos = vaihteluvali(lista) 
    tulos = vaihteluvali([1]) 
    print(tulos)