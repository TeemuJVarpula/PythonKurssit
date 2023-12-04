# TEE RATKAISUSI TÄHÄN:
from collections import Counter
class ListaApuri:

    def suurin_frekvenssi(lista: list):
        return Counter(lista).most_common(1)[0][0]

    def tuplia(lista: list):
        tuplat=[]
        
        for i in range (0,len(lista)):
            if lista.count(lista[i])>=2:
                if lista[i] not in tuplat:
                    tuplat.append(lista[i])

        return len(tuplat)      
    
if __name__ == "__main__":       
    luvut = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListaApuri.suurin_frekvenssi(luvut))
    print(ListaApuri.tuplia(luvut))