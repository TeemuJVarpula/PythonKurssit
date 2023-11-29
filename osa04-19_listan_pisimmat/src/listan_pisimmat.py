# tee ratkaisu tänne

def pisimmat(listaus):
    valitut=[""]

    for nimi in listaus:

        if  valitut[0]=="" or len(valitut[0])<len(nimi):
            #print(f"1 {len(valitut[0])} , {len(nimi)}")
            valitut=[nimi]
        elif len(valitut[0])==len(nimi):
            #print(f"2 {len(valitut[0])} , {len(nimi)}")
            valitut.append(nimi)
        #else:
            #print(f"3 {len(valitut[0])} , {len(nimi)}")
        
    
    return valitut


if __name__=="__main__":

    lista = ["eka", "toka", "kolmas", "seitsemäs"]

    tulos = pisimmat(lista)
    print(tulos) # ['seitsemäs']
    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]

    tulos = pisimmat(lista)
    print(tulos) # ['emilia', 'juhani']