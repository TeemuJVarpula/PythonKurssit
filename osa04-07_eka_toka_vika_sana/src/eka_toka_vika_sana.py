# tee ratkaisu tänne
def eka_sana(lause):

    index=lause.find(" ")
    sana=""

    for i in range(0,index):
        sana= sana+lause[i]
    return sana;

def toka_sana(lause):
    index=lause.find(" ")+1
    index2=lause.find(" ",index)
    sana=""
    if index2 == -1:
        index2=len(lause)
    for i in range(index,index2):
        sana= sana+lause[i]
    return sana;


def vika_sana(lause):
    index=lause.rfind(" ")+1
    sana=""

    for i in range(index,len(lause)):
        sana= sana+lause[i]
    return sana

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    lause = "olipa kerran kauan sitten ohjelmoija"
    print(eka_sana(lause)) # olipa
    print(toka_sana(lause)) # kerran
    print(vika_sana(lause)) # ohjelmoija

    print(toka_sana("eka toka")) # kerran