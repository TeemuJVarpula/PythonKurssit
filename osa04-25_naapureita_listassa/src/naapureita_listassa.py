# tee ratkaisu tänne

def pisin_naapurijono(lista):

    pituus=0
    laskuri=1

    for i in range(0,len(lista)-1):
        
        if lista[i]-lista[i+1]== 1 or lista[i]-lista[i+1]== -1:
            laskuri +=1
            if laskuri > pituus:
                pituus=laskuri
                
        else:
            laskuri=1
            
    return pituus


if __name__=="__main__":
    lista = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(pisin_naapurijono(lista))