# TEE RATKAISUSI TÄHÄN:
class Henkilo:
    def __init__(self, nimi: str, pituus: int):
        self.nimi = nimi
        self.pituus = pituus

    def __str__(self):
        return self.nimi

class Huone:
    def __init__(self):
        self.asukkaat=[]
    
    def lisaa(self,henkilo: Henkilo):
        self.asukkaat.append(henkilo)
        
    def on_tyhja(self):
        if len(self.asukkaat)==0:
            return True
        else:
            return False
        
    def tulosta_tiedot(self):
        
        if self.on_tyhja()==False:
            print(f"Huoneessa {len(self.asukkaat)} henkilöä, yhteispituus {sum(asukas.pituus for asukas in self.asukkaat)} cm")
        
        for henkilo in self.asukkaat:
            print(f"{henkilo} ({henkilo.pituus} cm)")
    
    def lyhin(self):
        
        if len(self.asukkaat)>0:
            lyhin=self.asukkaat[0]
            for henkilo in self.asukkaat:
                if lyhin=="" or henkilo.pituus < lyhin.pituus:
                    lyhin=henkilo

            return lyhin
        None
    def poista_lyhin(self):
        if len(self.asukkaat)>0:
            poistoon=0
            lyhin=self.asukkaat[0]
            
            for index in range(1,len(self.asukkaat)):
                
                #print({index})
                #print(f"{self.asukkaat[index-1].pituus} {self.asukkaat[index].pituus}")
                if lyhin.pituus>self.asukkaat[index].pituus:
                    lyhin=self.asukkaat[index]
                    poistoon=index
            
            self.asukkaat.pop(poistoon)
            return lyhin
        None
        
if __name__ == "__main__":
    # huone = Huone()
    # print("Huone tyhjä?", huone.on_tyhja())
    # huone.lisaa(Henkilo("Lea", 183))
    # huone.lisaa(Henkilo("Kenya", 182))
    # huone.lisaa(Henkilo("Auli", 186))
    # huone.lisaa(Henkilo("Nina", 172))
    # huone.lisaa(Henkilo("Terhi", 185))
    # print("Huone tyhjä?", huone.on_tyhja())
    # huone.tulosta_tiedot()
    
    # huone = Huone()

    # print("Huone tyhjä?", huone.on_tyhja())
    # print("Lyhin:", huone.lyhin())

    # huone.lisaa(Henkilo("Lea", 183))
    # huone.lisaa(Henkilo("Kenya", 182))
    # huone.lisaa(Henkilo("Nina", 172))
    # huone.lisaa(Henkilo("Auli", 186))

    # print()

    # print("Huone tyhjä?", huone.on_tyhja())
    # print("Lyhin:", huone.lyhin())

    # print()

    # huone.tulosta_tiedot()
    
    huone = Huone()

    huone.lisaa(Henkilo("Lea", 183))
    huone.lisaa(Henkilo("Kenya", 182))
    huone.lisaa(Henkilo("Nina", 172))
    huone.lisaa(Henkilo("Auli", 186))
    huone.tulosta_tiedot()

    print()

    poistettu = huone.poista_lyhin()
    print(f"Otettiin huoneesta {poistettu.nimi}")

    print()

    huone.tulosta_tiedot()
