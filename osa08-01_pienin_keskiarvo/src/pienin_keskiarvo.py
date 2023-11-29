# tee ratkaisu tänne
def pienin_keskiarvo(henkilo1: dict, henkilo2: dict, henkilo3: dict):

    henkilot=henkilo1,henkilo2,henkilo3
    pienin={}
    keskiarvo=0

    for henkilo in henkilot:
        print(pienin)
        if keskiarvo==0 or keskiarvo > (henkilo["tulos1"]+henkilo["tulos2"]+henkilo["tulos3"])/3:
            keskiarvo = (henkilo["tulos1"]+henkilo["tulos2"]+henkilo["tulos3"])/3
            pienin=henkilo
            
    return pienin


if __name__ == '__main__':
    henkilo1 = {"nimi": "Keijo", "tulos1": 2, "tulos2": 3, "tulos3": 3}
    henkilo2 = {"nimi": "Reijo", "tulos1": 5, "tulos2": 1, "tulos3": 8}
    henkilo3 = {"nimi": "Veijo", "tulos1": 3, "tulos2": 1, "tulos3": 1}

    print(pienin_keskiarvo(henkilo1, henkilo2, henkilo3))