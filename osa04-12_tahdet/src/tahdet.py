# tee ratkaisu tänne

def lista_tahtina(lista):
    
    for i in range(0,len(lista)):
        tahdet=""
        for j in range (0,lista[i]):
            tahdet=tahdet + "*"
        print (tahdet)
    

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
   lista_tahtina([3, 7, 1, 1, 2])
   lista_tahtina([2, 2])