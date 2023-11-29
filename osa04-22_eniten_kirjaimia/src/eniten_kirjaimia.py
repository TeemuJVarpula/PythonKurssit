# tee ratkaisu tänne

def eniten_kirjainta(lause):

    eniten=""
    lkm=0

    for merkki in lause:
            if lause.count(merkki)>lkm:
                eniten=merkki
                lkm=lause.count(merkki)
    
    return eniten


if __name__=="__main__":

    mjono = "abcbdbe"
    print(eniten_kirjainta(mjono))

    toinen_jono = "esimerkkimerkkijonokki"
    print(eniten_kirjainta(toinen_jono))