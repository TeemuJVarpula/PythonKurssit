# tee ratkaisu tänne

def poista_isot(lista):

    listaus=[]

    for sana in lista:
        if sana.isupper() != True:
            listaus.append(sana)
            
    return listaus


if __name__=="__main__":
    lista = ["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"]
    karsittu_lista = poista_isot(lista)
    print(karsittu_lista)