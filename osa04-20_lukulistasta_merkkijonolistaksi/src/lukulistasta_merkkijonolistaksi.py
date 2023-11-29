# tee ratkaisu tänne

def muotoile(listaus):

    listaX=[]

    for luku in listaus:
            listaX.append(f"{luku:.2f}")
    
    return listaX


if __name__=="__main__":

    lista = [1.234, 0.3333, 0.11111, 3.446]
    lista2 = muotoile(lista)
    print(lista2)