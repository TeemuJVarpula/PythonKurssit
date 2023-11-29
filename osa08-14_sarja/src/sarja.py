# Tee ratkaisusi tähän:

class Sarja:

    def __init__(self,nimi:str,kaudet:int,genret:list):
        self.nimi=nimi
        self.kaudet=kaudet
        self.genret=genret
        self.arvostelut=[]

    def arvostele(self,arvosana:int):
        self.arvostelut.append(arvosana)
    
    
    def __str__(self):
        arvostelut="ei arvosteluja"
        genrestr=", ".join(self.genret)
       
        if len(self.arvostelut)==0:
            keskiarvo=0
        else:
            keskiarvo=sum(self.arvostelut)/len(self.arvostelut)

        if len(self.arvostelut)>0:
            arvostelut=f"arvosteluja {len(self.arvostelut)}, keskiarvo {keskiarvo:.1f} pistettä"

        return f"{self.nimi} ({self.kaudet} esityskautta) \ngenret: {genrestr}\n{arvostelut}"


def arvosana_vahintaan(arvosana: float, sarjat: list):
    valitut=[]
    
    for sarja in sarjat:
        if sum(sarja.arvostelut)/len(sarja.arvostelut) > arvosana:
            valitut.append(sarja)
        
    return valitut

def sisaltaa_genren(genre: str, sarjat: list):
    valitut=[]
    
    for sarja in sarjat:
        if genre in sarja.genret:
            valitut.append(sarja)
        
    return valitut

if __name__ == "__main__":
    # dexter = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    # print(dexter)

    # dexter = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    # dexter.arvostele(4)
    # dexter.arvostele(5)
    # dexter.arvostele(5)
    # dexter.arvostele(3)
    # dexter.arvostele(0)
    # print(dexter)

    s1 = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.arvostele(5)

    s2 = Sarja("South Park", 24, ["Animation", "Comedy"])
    s2.arvostele(3)

    s3 = Sarja("Friends", 10, ["Romance", "Comedy"])
    s3.arvostele(2)

    sarjat = [s1, s2, s3]

    print("arvosana vähintään 4.5:")
    for sarja in arvosana_vahintaan(4.5, sarjat):
        print(sarja.nimi)
    print()
    print("genre Comedy:")
    for sarja in sisaltaa_genren("Comedy", sarjat):
        print(sarja.nimi)