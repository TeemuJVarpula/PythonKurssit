# Tee ratkaisusi tähän:
class Tavara:
    def __init__(self,nimi:str,paino:int=0):
        self.__nimi = nimi
        self.__paino = paino
    
    def __str__(self):
        return f"{self.__nimi} ({self.__paino} kg)"
    
    def nimi(self):
        return self.__nimi
    def paino(self):
        return int(self.__paino)
    
class Matkalaukku:
    def __init__(self,maksimi:float):
        self.__tavarat=[]
        self.__maksimi=maksimi
        
    def lisaa_tavara(self,lisattava:Tavara):
        if self.__maksimi>= self.paino() +lisattava.paino():
            self.__tavarat.append(lisattava)
            
    def __str__(self):
    
        if len(self.__tavarat) ==1:
            return f"{len(self.__tavarat)} tavara ({self.paino()} kg)"
        else:
            return f"{len(self.__tavarat)} tavaraa ({self.paino()} kg)"
    
    def tulosta_tavarat(self):
        for tavara in self.__tavarat:
            print(f"{tavara}")
            
    def paino(self):
        summa=0
        for tavara in self.__tavarat:
            summa= summa + tavara.paino()
        
        return int(summa)
    
    def raskain_tavara(self):
        if len(self.__tavarat) > 0:
            valittu=self.__tavarat[0]
                
            for tavara in self.__tavarat:
                if valittu.paino() < tavara.paino():
                    valittu=tavara
            
            return valittu
        None

class Lastiruuma:
    def __init__(self,maksimipaino:int):
        self.__laukut=[]
        self.__maksimi=maksimipaino
        
    def lisaa_matkalaukku(self,laukku:Matkalaukku):
        if self.__maksimi >= self.paino() +int(laukku.paino()):
            self.__laukut.append(laukku)
    
    def __str__(self):
        if len(self.__laukut) > 0:
            if len(self.__laukut) ==1:
                return f"{len(self.__laukut)} matkalaukku, tilaa {self.__maksimi-self.paino()} kg"
            else:
                return f"{len(self.__laukut)} matkalaukkua, tilaa {self.__maksimi-self.paino()} kg"
        else:
            return f"0 matkalaukkua, tilaa {self.__maksimi} kg"
            
    def paino(self):
        summa=0
        for laukku in self.__laukut:
            summa= summa + laukku.paino()
        
        return int(summa)
    
    def tulosta_tavarat(self):
        if len(self.__laukut) > 0:
            for laukku in self.__laukut:
                laukku.tulosta_tavarat()
        else:
            print(f"0 matkalaukkua, tilaa {self.__maksimi} kg")
            
if __name__ == "__main__":
    # kirja = Tavara("Aapiskukko", 2)
    # puhelin = Tavara("Nokia 3210", 1)

    # print("Kirjan nimi:", kirja.nimi())
    # print("Kirjan paino:", kirja.paino())

    # print("Kirja:", kirja)
    # print("Puhelin:", puhelin)
    
    
    # kirja = Tavara("Aapiskukko", 2)
    # print(id(kirja.paino()))
    # kirja.paino = 10
    # print(id(kirja.paino))
    
    
    # kirja = Tavara("Aapiskukko", 2)
    # puhelin = Tavara("Nokia 3210", 1)
    # tiiliskivi = Tavara("Tiiliskivi", 4)

    # matkalaukku = Matkalaukku(5)
    # print(matkalaukku)

    # matkalaukku.lisaa_tavara(kirja)
    # print(matkalaukku)

    # matkalaukku.lisaa_tavara(puhelin)
    # print(matkalaukku)

    # matkalaukku.lisaa_tavara(tiiliskivi)
    # print(matkalaukku)
    
    
    # kirja = Tavara("Aapiskukko", 2)
    # puhelin = Tavara("Nokia 3210", 1)
    # tiiliskivi = Tavara("Tiiliskivi", 4)

    # matkalaukku = Matkalaukku(10)
    # matkalaukku.lisaa_tavara(kirja)
    # matkalaukku.lisaa_tavara(puhelin)
    # matkalaukku.lisaa_tavara(tiiliskivi)

    # print("Matkalaukussa on seuraavat tavarat:")
    # matkalaukku.tulosta_tavarat()
    # paino_yht = matkalaukku.paino()
    # print(f"Yhteispaino: {paino_yht} kg")
    
    
    # kirja = Tavara("Aapiskukko", 2)
    # puhelin = Tavara("Nokia 3210", 1)
    # tiiliskivi = Tavara("Tiiliskivi", 4)

    # matkalaukku = Matkalaukku(10)
    # matkalaukku.lisaa_tavara(kirja)
    # matkalaukku.lisaa_tavara(puhelin)
    # matkalaukku.lisaa_tavara(tiiliskivi)

    # raskain = matkalaukku.raskain_tavara()
    # print(f"Raskain tavara: {raskain}")
    
    
    # lastiruuma = Lastiruuma(1000)
    # print(lastiruuma)

    # kirja = Tavara("Aapiskukko", 2)
    # puhelin = Tavara("Nokia 3210", 1)
    # tiiliskivi = Tavara("Tiiliskivi", 4)

    # adan_laukku = Matkalaukku(10)
    # adan_laukku.lisaa_tavara(kirja)
    # adan_laukku.lisaa_tavara(puhelin)

    # pekan_laukku = Matkalaukku(10)
    # pekan_laukku.lisaa_tavara(tiiliskivi)

    # lastiruuma.lisaa_matkalaukku(adan_laukku)
    # print(lastiruuma)

    # lastiruuma.lisaa_matkalaukku(pekan_laukku)
    # print(lastiruuma)
    
    
    
    kirja = Tavara("Aapiskukko", 2)
    puhelin = Tavara("Nokia 3210", 1)
    tiiliskivi = Tavara("Tiiliskivi", 4)

    adan_laukku = Matkalaukku(10)
    adan_laukku.lisaa_tavara(kirja)
    adan_laukku.lisaa_tavara(puhelin)

    # pekan_laukku = Matkalaukku(10)
    # pekan_laukku.lisaa_tavara(tiiliskivi)

    # lastiruuma = Lastiruuma(1000)
    # lastiruuma.lisaa_matkalaukku(adan_laukku)
    # lastiruuma.lisaa_matkalaukku(pekan_laukku)

    # print("Ruuman matkalaukuissa on seuraavat tavarat:")
    # lastiruuma.tulosta_tavarat()

    ruuma = Lastiruuma(100)
    print(ruuma)