# tee ratkaisu tänne
def rivien_summat(matriisi: list):

    for i in range (0,len(matriisi)):
        summa=0
        for alkio in matriisi[i]:
            summa= summa+alkio

        matriisi[i].append(summa)



if __name__ == '__main__':
    matriisi = [[1, 2], [3, 4]]
    rivien_summat(matriisi)
    print(matriisi)