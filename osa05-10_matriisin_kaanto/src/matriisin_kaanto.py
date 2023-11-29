# tee ratkaisu tänne
def transponoi(matriisi: list):
    muutettu=[]
    laskuri=0
    
    #setting matrix size
    for r in matriisi: muutettu.append(r[:])

    #Copying values
    for rivi in range(0,len(matriisi)):
        for sarake in range(0,len(matriisi)):
            matriisi[sarake][rivi]=muutettu[rivi][sarake]


if __name__ == "__main__":

    matriisi = [[4, 3, 2], [2, 3, 4], [5, 3, 2]]
    uusimatriisi=transponoi(matriisi)

    print(matriisi)
    print(uusimatriisi)