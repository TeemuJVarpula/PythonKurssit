# tee ratkaisu tänne
def lue_hedelmat():
    with open("hedelmat.csv") as tiedosto:
        sanakirja={}
        sisalto=""

        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            sisalto=rivi.split(";")

            print(sisalto[0])
            print(sisalto[1])
            sanakirja[sisalto[0]]=float(sisalto[1])
            
        return sanakirja



if __name__ == "__main__":

    print(lue_hedelmat())