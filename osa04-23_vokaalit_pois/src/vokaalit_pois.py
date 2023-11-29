# tee ratkaisu tänne

def ilman_vokaaleja(lause):

    lause2=""

    for merkki in lause:
            if merkki =="a" or merkki =="e" or merkki =="i" or merkki =="o" or merkki =="u" or merkki =="y" or merkki =="å" or merkki =="ä" or merkki =="ö":
                print(merkki)
            else:
                lause2= lause2+(merkki)
    return lause2


if __name__=="__main__":
    mjono = "tämä on esimerkki"
    print(ilman_vokaaleja(mjono))
    print(ilman_vokaaleja("abcdefghijklmnopqrstuvwxyzåäö"))