# Tee ratkaisusi tähän:

class Tehtava():
    nextid = 1
    # @classmethod 
    # def uusi_id(cls):
    #     Tehtava.id += 1
    #     return Tehtava.id
    
    def __init__(self,kuvaus:str,koodari:str,tyomaara:int):
        self.kuvaus=kuvaus
        self.koodari =koodari
        self.tyomaara = tyomaara
        self.__valmis = False
        self.id = Tehtava.nextid
        Tehtava.nextid +=1
        
    def on_valmis(self):
        return self.__valmis
    
    def merkkaa_valmiiksi(self):
        self.__valmis = True
        
    def __str__(self):
        if self.on_valmis() == True:
            valmis= "VALMIS"
        else:    
            valmis= "EI VALMIS"
        #status = "EI VALMIS" if not self.valmis else "VALMIS"
        return f"{self.id}: {self.kuvaus} ({self.tyomaara} tuntia), koodari {self.koodari} {valmis}"

class Tilauskirja():
    def __init__(self):
        self.__tilaukset=[]
        Tehtava.nextid=1
    
    def lisaa_tilaus(self,kuvaus:str,koodari:str,tyomaara:int):
        self.__tilaukset.append(Tehtava(kuvaus,koodari,tyomaara))
        
    def kaikki_tilaukset(self):
        return [tilaus for tilaus in self.__tilaukset]
    
    def koodarit(self):
        return list(set([tilaus.koodari for tilaus in self.__tilaukset]))
            
    def __iter__(self):
        self.__laskuri=0
        return self
    
    def __next__(self):
        if(self.__laskuri >= len(self.__tilaukset)):
            raise StopIteration
        self.__laskuri += 1
        return self.__laskuri
    
    def merkkaa_valmiiksi(self, id: int):
        for i in range (0,len(self.__tilaukset)):
            if self.__tilaukset[i].id == id:
                print (f"{self.__tilaukset[i].id} -> {id}")
                self.__tilaukset[i].merkkaa_valmiiksi()
                return
        
        raise ValueError(f"Ei kyseistä tehtävää")
    
    def __str__(self):
        return f"Tilauskirja: {len(self.__tilaukset)} tilausta"
        
    def valmiit_tilaukset(self):
        return [tilaus for tilaus in self.__tilaukset if tilaus.on_valmis()==True]
    def ei_valmiit_tilaukset(self):
        return [tilaus for tilaus in self.__tilaukset if tilaus.on_valmis()==False]
    
    def koodarin_status(self, koodari: str):

        if koodari in self.koodarit():
            tyot= [tilaus for tilaus in self.__tilaukset if tilaus.koodari == koodari]
            valmiit=0
            kesken=0
            valmiitarviot=0
            keskenarviot=0
            
            for tyo in tyot:
                if tyo.on_valmis() == True:
                    valmiit +=1
                    valmiitarviot = valmiitarviot + tyo.tyomaara
                else:
                    kesken +=1
                    keskenarviot = keskenarviot + tyo.tyomaara   
            
            return (valmiit,kesken,valmiitarviot,keskenarviot)
        
        else:
            raise ValueError("Ei kyseistä koodaria")
        
    
if __name__ == "__main__": 
    # t1 = Tehtava("koodaa hello world", "Erkki", 3)
    # print(t1.id, t1.kuvaus, t1.koodari, t1.tyomaara)
    # print(t1)
    # print(t1.on_valmis())
    # t1.merkkaa_valmiiksi()
    # print(t1)
    # print(t1.on_valmis())
    # t2 = Tehtava("koodaa webbikauppa", "Antti", 10)
    # t3 = Tehtava("tee mobiilisovellus työaikakirjanpitoon", "Erkki", 25)
    # print(t2)
    # print(t3)
    
    # tilaukset = Tilauskirja()
    # tilaukset.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
    # tilaukset.lisaa_tilaus("tee mobiilisovellus työaikakirjanpitoon", "Erkki", 25)
    # tilaukset.lisaa_tilaus("tee ohjelma matematiikan harjoitteluun", "Antti", 100)
    # for tilaus in tilaukset.kaikki_tilaukset():
    #     print(tilaus)
    # for koodari in tilaukset.koodarit():
    #     print(koodari)
        
    # tilaukset = Tilauskirja()
    # tilaukset.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
    # tilaukset.lisaa_tilaus("tee mobiilisovellus työaikakirjanpitoon", "Erkki", 25)
    # tilaukset.lisaa_tilaus("tee ohjelma matematiikan harjoitteluun", "Antti", 100)
    # tilaukset.merkkaa_valmiiksi(1)
    # tilaukset.merkkaa_valmiiksi(2)
    # for tilaus in tilaukset.kaikki_tilaukset():
    #     print(tilaus)
        
    # tilaukset = Tilauskirja()
    # tilaukset.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
    # tilaukset.lisaa_tilaus("tee mobiilisovellus työaikakirjanpitoon", "Antti", 25)
    # tilaukset.lisaa_tilaus("tee ohjelma matematiikan harjoitteluun", "Antti", 100)
    # tilaukset.lisaa_tilaus("tee uusi facebook", "Erkki", 1000)
    # tilaukset.merkkaa_valmiiksi(1)
    # tilaukset.merkkaa_valmiiksi(2)
    # status = tilaukset.koodarin_status("Antti")
    # print(status)
    
    # t = Tilauskirja()
    # t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
    # t.merkkaa_valmiiksi(999)
    
    t = Tilauskirja()
    t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
    t.lisaa_tilaus("koodaa parempi facebook", "joona", 5000)
    t.lisaa_tilaus("tee mobiilipeli", "Erkki", 5)
    t.merkkaa_valmiiksi(1)
    t.merkkaa_valmiiksi(2)
    t.ei_valmiit_tilaukset()
    
    til=t.kaikki_tilaukset()
    for tilaus in til:
        print(tilaus)
    t.merkkaa_valmiiksi(2)
    print()
    for tilaus in t.ei_valmiit_tilaukset():
        print(tilaus)
