# tee ratkaisusi tänne
class Suoritus:
    def __init__(self,kurssi:str,arvosana:int,pisteet:int):
        self.__kurssi=kurssi
        self.__arvosana=arvosana
        self.__pisteet=pisteet
    
    def nimi(self):
        return self.__kurssi
    
    def arvosana(self):
        return int(self.__arvosana)
    
    def opintopisteet(self):
        return int(self.__pisteet)
    
    def muuta_arvosana(self,arvosana):
        
        if self.__arvosana<arvosana:
            self.__arvosana=arvosana
        
    
    def __str__(self):
        return(f"{self.__kurssi} ({self.__pisteet} op) arvosana {self.__arvosana}")
        
class Suoritukset:
    def __init__(self):
        self.__suoritukset={}
        self.__suorituksia=0
        
    def lisaa_suoritus(self,kurssi,arvosana,pisteet):
        if kurssi not in self.__suoritukset:
            self.__suoritukset[kurssi]=Suoritus(kurssi,arvosana,pisteet)
            self.__suorituksia+=1
        else:
            self.__suoritukset[kurssi].muuta_arvosana(arvosana)
    
    def hae_suoritus(self,kurssi:str):
        if kurssi not in self.__suoritukset:
            return "ei suoritusta"
        else:
            return self.__suoritukset[kurssi]
        
    def keskiarvo(self):
        summa=0

        for kurssi in self.__suoritukset:
            summa= summa+self.__suoritukset[kurssi].arvosana()
        return f"{(summa/self.__suorituksia):.1f}"
    
    def opintopisteet(self):
        opintopisteet=0
        
        for kurssi in self.__suoritukset:
            opintopisteet= opintopisteet+self.__suoritukset[kurssi].opintopisteet()
            
        return (self.__suorituksia,opintopisteet)
    
    def jakauma(self):
        jakauma=["","","","","",""]
        
        for kurssi in self.__suoritukset:
            jakauma[int(self.__suoritukset[kurssi].arvosana())] += "x"

        return jakauma
    
class Valikko:
    
    def __init__(self):
        self.__luettelo = Suoritukset()

    def ohje(self):
        print("1 lisää suoritus")
        print("2 hae suoritus")
        print("3 tilastot")
        print("0 lopetus")
        
    def suorituksen_lisays(self):
        kurssi = input("kurssi: ")
        arvosana = input("arvosana: ")
        opintopisteet =input("opintopisteet: ")
        self.__luettelo.lisaa_suoritus(kurssi,arvosana,opintopisteet) 
        
    def suorituksen_haku(self):
        kurssi = input("kurssi: ")
        print(self.__luettelo.hae_suoritus(kurssi))
    
    def tilaston_tulostus(self):
        pisteet=self.__luettelo.opintopisteet()
        print(f"suorituksia {pisteet[0]} kurssilta, yhteensä {pisteet[1]} opintopistettä")
        
        keskiarvo=self.__luettelo.keskiarvo()
        print(f"keskiarvo {keskiarvo}")
        
        arvosanajakauma=self.__luettelo.jakauma()
        print("arvosanajakauma")
        print(f"5: {arvosanajakauma[5]}")
        print(f"4: {arvosanajakauma[4]}")
        print(f"3: {arvosanajakauma[3]}")
        print(f"2: {arvosanajakauma[2]}")
        print(f"1: {arvosanajakauma[1]}")
        
    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.suorituksen_lisays()
            elif komento == "2":
                self.suorituksen_haku()
            elif komento == "3":
                self.tilaston_tulostus()
            else:
                self.ohje()
                

# kun testaat, mitään muuta koodia ei saa olla luokkien ulkopuolella kuin seuraavat rivit
sovellus = Valikko()
sovellus.suorita()
