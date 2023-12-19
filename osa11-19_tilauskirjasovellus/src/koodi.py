# tee ratkaisusi tänne
# jos käytät edellisessä tehtävässä tekemiäsi luokkia, kopioi ne tänne
class Tehtava:
    id =0
    
    @classmethod 
    def uusi_id(cls):
        Tehtava.id += 1
        return Tehtava.id
    
    def __init__(self,kuvaus:str,koodari:str,tyomaara:int):
        self.kuvaus=kuvaus
        self.koodari =koodari
        self.tyomaara = tyomaara
        self.__valmis = False
        self.id = Tehtava.uusi_id()
        
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
        
    
class valikko:

    def __init__(self):
        self.__Tilaukset = Tilauskirja()

    def ohje(self):
        print("komennot: ")
        print("0 lopetus")
        print("1 lisää tilaus")
        print("2 listaa valmiit")
        print("3 listaa ei valmiit")
        print("4 merkitse tehtävä valmiiksi")
        print("5 koodarit")
        print("6 koodarin status")

    def lisaa_tilaus(self):
        kuvaus = input("kuvaus: ")
        tekija_tunnit =(input("koodari ja työmääräarvio: ")).split()

        if len(tekija_tunnit)==2:
            (koodari,tyomaara)= tekija_tunnit
            if tyomaara.isnumeric()==True:
                self.__Tilaukset.lisaa_tilaus(kuvaus, koodari,int(tyomaara))
                print("lisätty!")
                return

        print("virheellinen syöte\n")
        
    def listaa_valmiit(self):
        if self.__Tilaukset.valmiit_tilaukset() != []:
            for tehtava in self.__Tilaukset.valmiit_tilaukset():
                print(tehtava)
        else: 
            print("ei valmiita")
            
    def listaa_eivalmiit(self):  
        if self.__Tilaukset.ei_valmiit_tilaukset() != []:
            for tehtava in self.__Tilaukset.ei_valmiit_tilaukset():
                print(tehtava)
        else: 
            print("Ei keskenräisiä")
        
    def merkitse_valmiiksi(self):
        tunniste = input("tunniste: ")
        if tunniste.isnumeric()==True and int (tunniste) > 0 and int(tunniste) <= len(self.__Tilaukset.kaikki_tilaukset()):
            self.__Tilaukset.merkkaa_valmiiksi(int(tunniste))
            print("merkitty valmiiksi")
            return
        
        print("virheellinen syöte\n")
        
    def listaa_koodarit(self):
        if self.__Tilaukset.koodarit() != []:
            for koodari in self.__Tilaukset.koodarit():
                print (koodari)
        else:
            print("ei koodareita")
            
    def listaa_koodaristatus(self):
        koodari = input("koodari: ")
        try:
            (valmiit,kesken,valmiitarviot,keskenarviot)=self.__Tilaukset.koodarin_status(koodari)
            print(f"työt: valmiina {valmiit} ei valmiina {kesken}, tunteja: tehty {valmiitarviot} tekemättä {keskenarviot}")
        except:
            print("virheellinen syöte\n")
            
        
        
    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.lisaa_tilaus()
            elif komento == "2":
                self.listaa_valmiit()
            elif komento == "3":
                self.listaa_eivalmiit()
            elif komento == "4":
                self.merkitse_valmiiksi()
            elif komento == "5":
                self.listaa_koodarit()
            elif komento == "6":
                self.listaa_koodaristatus()
            else:
                self.ohje()
                

# kun testaat, mitään muuta koodia ei saa olla luokkien ulkopuolella kuin seuraavat rivit
sovellus = valikko()
sovellus.suorita()