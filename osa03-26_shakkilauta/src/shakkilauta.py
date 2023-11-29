# tee ratkaisu tänne
def shakkilauta(koko):
    vuorossa=1

    for i in range(0,koko):
        rivi=""
        for i in range(0,koko):
            if vuorossa==1:
                rivi=rivi+("1")
                vuorossa=0
            else:
                rivi=rivi+("0")
                vuorossa=1
        print(rivi)

        if koko%2==0:
            if vuorossa==1:
                vuorossa=0
            else:
                vuorossa=1

    


# kokeillaan funktiota kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    shakkilauta(2)

    shakkilauta(4)
    shakkilauta(6)