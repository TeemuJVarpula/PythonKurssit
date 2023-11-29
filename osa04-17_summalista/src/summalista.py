# tee ratkaisu tänne
def summa(lista,lista2):
    
    listaus=[]

    for i in range(0,len(lista)):
        listaus.append(lista[i]+lista2[i])

    return listaus

if __name__ == "__main__":
    
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(summa(a, b)) # [8, 10, 12]