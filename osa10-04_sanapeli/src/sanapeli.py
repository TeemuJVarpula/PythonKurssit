# TEE RATKAISUSI TÄHÄN:
import random

class Sanapeli():
    def __init__(self, kierrokset: int):
        self.voitot1 = 0
        self.voitot2 = 0
        self.kierrokset = kierrokset

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        # arvotaan voittaja
        return random.randint(1, 2)

    def pelaa(self):
        print("Sanapeli:")
        for i in range(1, self.kierrokset+1):
            print(f"kierros {i}")
            vastaus1 = input("pelaaja1: ")
            vastaus2 = input("pelaaja2: ")

            if self.kierroksen_voittaja(vastaus1, vastaus2) == 1:
                self.voitot1 += 1
                print("pelaaja 1 voitti")
            elif self.kierroksen_voittaja(vastaus1, vastaus2) == 2:
                self.voitot2 += 1
                print("pelaaja 2 voitti")
            else:
                pass # tasapeli

        print("peli päättyi, voitot:")
        print(f"pelaaja 1: {self.voitot1}")
        print(f"pelaaja 2: {self.voitot2}")

class PisinSana(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        # tänne voittajan ratkaiseva koodi
        if len(pelaaja1_sana) > len(pelaaja2_sana):
            return 1
        elif len(pelaaja1_sana) < len(pelaaja2_sana):
            return 2

class EnitenVokaaleja(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)
    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):   
        p1_vokaalit = sum([pelaaja1_sana.count(x) for x in "aeiouyäöå"])
        p2_vokaalit = sum([pelaaja2_sana.count(y) for y in "aeiouyäöå"])
        
        if p1_vokaalit > p2_vokaalit:
            print(f"{p1_vokaalit} > {p2_vokaalit}")
            return 1
        elif p1_vokaalit < p2_vokaalit:
            print(f"{p1_vokaalit} < {p2_vokaalit}")
            return 2

class KiviPaperiSakset(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)
    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        
        taulukko=["kivi","sakset","paperi"]
        
        if pelaaja1_sana in taulukko and pelaaja2_sana not in taulukko:
            return 1
        elif pelaaja2_sana in taulukko and pelaaja1_sana not in taulukko:
            return 2
        elif pelaaja1_sana != pelaaja2_sana and pelaaja2_sana in taulukko and pelaaja1_sana in taulukko:
            if pelaaja1_sana==taulukko[0]:
                if pelaaja2_sana==taulukko[1]:
                    return 1
                else:
                    return 2
            elif pelaaja1_sana==taulukko[1]:
                if pelaaja2_sana==taulukko[2]:
                    return 1
                else:
                    return 2
            if pelaaja1_sana==taulukko[2]:
                if pelaaja2_sana==taulukko[0]:
                    return 1
                else:
                    return 2

if __name__ == "__main__":
    # p = Sanapeli(3)
    # p.pelaa()
    
    # print ( "Pisin sana:")
    # r = PisinSana(2)
    # r.pelaa()
    
    # print ( "EnitenVokaaleja:")
    # s = EnitenVokaaleja(2)
    # s.pelaa()

    print ( "KiviPaperiSakset:")
    s = KiviPaperiSakset(4)
    s.pelaa()
    