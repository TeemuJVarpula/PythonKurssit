# tee ratkaisu tänne
def nelio(sana,koko):
    vuorossa=0

    for i in range(0,koko):
        rivi=""
        for i in range(0,koko):
                rivi=rivi+sana[vuorossa]
                vuorossa +=1
                if vuorossa==len(sana):
                    vuorossa=0
        print(rivi)

# kokeillaan funktiota kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":

    nelio("ab", 3)
    nelio("aybabtu", 5)
