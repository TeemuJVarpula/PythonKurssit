# ÄLÄ MUUTA ALLA OLEVAA LUOKKAA Kauppalista!
# Kirjoita ratkaisusi luokan alapuolelle!
class Kauppalista:
    def __init__(self):
        self.tuotteet = []

    def tuotteita(self):
        return len(self.tuotteet)

    def lisaa(self, tuote: str, maara: int):
        self.tuotteet.append((tuote, maara))

    def tuote(self, n: int):
        return self.tuotteet[n - 1][0]

    def maara(self, n: int):
        return self.tuotteet[n - 1][1]

# ----------------------
# Tee ratkaisusi tähän:
# ----------------------

def tuotteita_yhteensa(lista: Kauppalista):

    laskuri=0
    maara=lista.tuotteita()
    for i in range(1,maara+1):
        laskuri=laskuri+(lista.maara(i))
    return laskuri


if __name__ == '__main__':

    lista = Kauppalista()
    lista.lisaa("banaanit", 10)
    lista.lisaa("omenat", 5)
    lista.lisaa("ananas", 1)

    
    print(lista.tuotteita())
    print(lista.tuote(1))
    print(lista.maara(1))
    print(lista.tuote(2))
    print(lista.maara(2))

    # kauppalistalla tuotteet on indeksöity ykkösestä alkaen
    for i in range(1, lista.tuotteita()+1):
        tuote = lista.tuote(i)
        maara = lista.maara(i)
        print(f"{tuote}: {maara} kpl")
        
    print(f"Tuotteita yhteensä: {tuotteita_yhteensa(lista)}")