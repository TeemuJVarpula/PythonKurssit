# tee ratkaisu tänne
def poista_pienin(luvut:list):
    pienin=0

    for i in range(1,len(luvut)):
        if luvut[i]< luvut[pienin]:
            pienin = i
    
    luvut.pop(pienin)


if __name__ == "__main__":
    luvut = [2, 4, 6, 1, 3, 5]
    poista_pienin(luvut)
    print(luvut)