# tee ratkaisu tänne
def tuplaa_alkiot(lista:list):
    lista2=[]

    for i in lista:
        lista2.append(2*i)
    
    return lista2
    


if __name__ == "__main__":
    luvut = [2, 4, 5, 3, 11, -4]
    tuplaluvut = tuplaa_alkiot(luvut)
    print("alkuperäinen:", luvut)
    print("tuplattu:", tuplaluvut)