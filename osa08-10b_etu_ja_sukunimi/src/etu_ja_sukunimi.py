# Tee ratkaisusi tähän:

class Henkilo:
    def __init__(self, arvo_alussa: int):
        self.nimi=arvo_alussa

    def anna_etunimi(self):
        return self.nimi.split()[0]
    def anna_sukunimi(self):
        return self.nimi.split()[-1]


if __name__ == "__main__":
    pekka = Henkilo("Pekka Python")
    print(pekka.anna_etunimi())
    print(pekka.anna_sukunimi())

    pauli = Henkilo("Pauli Pythonen")
    print(pauli.anna_etunimi())
    print(pauli.anna_sukunimi())


