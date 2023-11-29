# tee ratkaisu tänne

def parilliset(listaus):

    parilliset=[]

    for i in range(0,len(listaus)):
        if listaus[i]%2==0:
            parilliset.append(listaus[i])

    return parilliset


if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    uusi_lista = parilliset(lista)
    print("alkuperäinen", lista)
    print("uusi", uusi_lista)