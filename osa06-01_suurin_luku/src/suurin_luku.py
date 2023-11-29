# tee ratkaisu tänne
def suurin():
    with open("luvut.txt") as tiedosto:
        suurin = 0

        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            
            if int(rivi)>suurin:
                suurin= int(rivi)
            
        return suurin



if __name__ == "__main__":

    print(suurin())