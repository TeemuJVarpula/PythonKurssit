# tee ratkaisu tänne

def lyhin(listaus):
    valittu=listaus[0]

    for i in range(1,len(listaus)):
        if  len(listaus[i]) < len(valittu):
            valittu=listaus[i]
    
    return valittu


if __name__=="__main__":

    lista = ["eka", "toka", "kolmas", "seitsemäs"]

    tulos = lyhin(lista)
    print(tulos)
    lista = ["pekka", "emilia", "johanna", "venla", "eero", "antti"]

    tulos = lyhin(lista)
    print(tulos)    