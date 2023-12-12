
# Tee ratkaisusi tähän:

class Henkilo():
    def __init__(self,nimi:str): 
        self.__nimi= nimi
        self.__osoite = None
        self.__numerot = []
        
    def nimi(self):
        return self.__nimi
    
    def numerot(self):
        return self.__numerot
    
    def lisaa_numero(self, numero: str):
        self.__numerot.append(numero)
    
    def osoite(self):
        return self.__osoite
    
    def lisaa_osoite(self,osoite:str):
        self.__osoite  = osoite
    
    def __str__(self):
        return f"Nimi: {self.__nimi} Osoite: {self.__osoite} Numerot: {self.numerot()}"
        
# # kun testaat, mitään muuta koodia ei saa olla luokkien ulkopuolella kuin seuraavat rivit
# sovellus = PuhelinluetteloSovellus()
class Puhelinluettelo:
    def __init__(self):
        self.__henkilot = {}

    def lisaa_numero(self, nimi: str, numero: str):
        if  nimi not in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)
        self.__henkilot[nimi].lisaa_numero(numero)
        
    def lisaa_osoite(self, nimi: str, osoite: str):
        if  nimi not in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)
        self.__henkilot[nimi].lisaa_osoite(osoite)
        
    def hae_tiedot(self, nimi: str):
        if nimi not in self.__henkilot:
            return None
        else:
            numerot=""
            for numero in self.__henkilot[nimi].numerot():
                numerot = numerot + numero
            print(f"{len(numerot)} 1{numerot}1")        
            if len(numerot) == 0:
                numerot = "numero ei tiedossa"                
                
            if self.__henkilot[nimi].osoite() == None:
                osoite = "osoite ei tiedossa"
            else:
                osoite = self.__henkilot[nimi].osoite()
                
            return {f"{numerot}\n{osoite}"}

            #return self.__henkilot[nimi]

    def kaikki_tiedot(self):
        return self.__henkilot
        
class PuhelinluetteloSovellus:
    def __init__(self):
        self.__luettelo = Puhelinluettelo()

    def ohje(self):
        print("komennot: ")
        print("0 lopetus")
        print("1 numeron lisäys")
        print("2 haku")
        print("3 osoitteen lisäys")
        
    def osoitteen_lisays(self):
        nimi = input("nimi: ")
        numero = input("osoite: ")
        self.__luettelo.lisaa_osoite(nimi, numero)

    def numeron_lisays(self):
        nimi = input("nimi: ")
        osoite = input("numero: ")
        self.__luettelo.lisaa_numero(nimi, osoite)
    
    def haku(self):
        nimi = input("nimi: ")
        henkilot = self.__luettelo.hae_tiedot(nimi)
        if henkilot == None:
            print("numero ei tiedossa\nosoite ei tiedossa") 
            return 
        for henkilo in henkilot:
            print(henkilo)       

    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.numeron_lisays()
            elif komento == "2":
                self.haku()
            elif komento == "3":
                self.osoitteen_lisays()
            else:
                self.ohje()
                

# kun testaat, mitään muuta koodia ei saa olla luokkien ulkopuolella kuin seuraavat rivit
sovellus = PuhelinluetteloSovellus()
sovellus.suorita()

#if __name__ == "__main__": 
    # henkilo = Henkilo("Erkki")
    # print(henkilo.nimi())
    # print(henkilo.numerot())
    # print(henkilo.osoite())
    # henkilo.lisaa_numero("040-123456")
    # henkilo.lisaa_osoite("Mannerheimintie 10 Helsinki")
    # print(henkilo.numerot())
    # print(henkilo.osoite())
    
    # luettelo = Puhelinluettelo()
    # luettelo.lisaa_numero("Erkki", "02-123456")
    # print(luettelo.hae_tiedot("Erkki"))
    # print(luettelo.hae_tiedot("Emilia"))
    
    # h = Henkilo("Erkki")
    # h.numerot()