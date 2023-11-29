# tee ratkaisu tänne
def vanhin(henkilot: list):
    vanhin = (0,0)
    for henkilo in henkilot:
        
        if henkilo[1] < vanhin[1] or vanhin[1] ==0:
            vanhin = henkilo

    return vanhin[0]

def vanhemmat(henkilot: list, vuosi: int):

    henkilolista=[]

    for henkilo in henkilot:
        
        if henkilo[1] < vuosi:
            henkilolista.append(henkilo[0])

    return henkilolista


if __name__ == "__main__":   

    h1 = ("Arto", 1977)
    h2 = ("Einari", 1985)
    h3 = ("Maija", 1953)
    h4 = ("Essi", 1997)
    hlista = [h1, h2, h3, h4]

    vanhemmat_henkilot = vanhemmat(hlista, 1979)
    print(vanhemmat_henkilot)