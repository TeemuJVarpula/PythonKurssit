# tee ratkaisu tänne
def positiivisten_summa(listaus):
    summa=0


    for i in range(0,len(listaus)):
        if listaus[i]>-1:
            summa=summa+listaus[i]

    return summa

if __name__ == "__main__":
    
    lista = [1, -2, 3, -4, 5]
    vastaus = positiivisten_summa(lista)
    print("vastaus", vastaus)