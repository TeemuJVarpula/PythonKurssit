# TEE RATKAISUSI TÄHÄN:
import re
def yleisimmat_sanat(tiedoston_nimi: str, raja: int):
    with open (tiedoston_nimi,"r") as file:
        sanalista=(file.read()).split()
        sanalista=[re.sub("[.,$@&€™-]","",sana) for sana in sanalista]
        
    #return {sana:sanalista.count(sana) for sana in sanalista}
    return {sana:sanalista.count(sana) for sana in sanalista if sanalista.count(sana)>=raja}
    
if __name__ == "__main__": 
    kirja=yleisimmat_sanat("comprehensions.txt", 3)
    print(kirja)
    kirja2=yleisimmat_sanat("programming.txt", 4)
    print(kirja2)