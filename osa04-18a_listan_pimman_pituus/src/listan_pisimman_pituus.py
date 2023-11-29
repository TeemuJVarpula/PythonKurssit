# tee ratkaisu tänne

def pisimman_pituus(listaus):
    pisin=0

    for i in range(0,len(listaus)):
        if  int(len(listaus[i])) > pisin:
            pisin=int(len(listaus[i]))
    
    return pisin


if __name__=="__main__":

    lista = ["eka", "toka", "kolmas", "seitsemäs"]

    tulos = pisimman_pituus(lista)
    print(tulos)

    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]

    tulos = pisimman_pituus(lista)
    print(tulos)

    lista = ['Arto', 'Leena', 'Santeri', 'Kim', 'Minna']

    tulos = pisimman_pituus(lista)
    print(tulos)