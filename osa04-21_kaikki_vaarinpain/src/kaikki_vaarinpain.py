# tee ratkaisu tänne

def kaikki_vaarinpain(listaus):

    vaarinpain=[]

    for sanat in listaus:
            vaarinpain.insert(0,(sanat[::-1]))
    
    return vaarinpain


if __name__=="__main__":

    lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
    lista2 = kaikki_vaarinpain(lista)
    print(lista2)