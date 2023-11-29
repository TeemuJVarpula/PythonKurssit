# Tee ratkaisusi tähän:
class  Lukutilasto:
    def __init__(self):
        self.lukuja = 0
        self.laskettu = 0

    def lisaa_luku(self, luku:int):
        self.lukuja +=1
        self.laskettu += int(luku)

    def lukujen_maara(self):
        return self.lukuja
    
    def summa(self):
        if self.lukuja==0:
            return 0
        else:
            return self.laskettu
    
    def keskiarvo(self):
        if self.lukuja==0:
            return 0
        else:
            return self.laskettu/self.lukuja


# tilasto = Lukutilasto()
# tilasto.lisaa_luku(3)
# tilasto.lisaa_luku(5)
# tilasto.lisaa_luku(1)
# tilasto.lisaa_luku(2)
# print("Lukujen määrä:", tilasto.lukujen_maara())

# tilasto = Lukutilasto()
# tilasto.lisaa_luku(3)
# tilasto.lisaa_luku(5)
# tilasto.lisaa_luku(1)
# tilasto.lisaa_luku(2)
# print("Lukujen määrä:", tilasto.lukujen_maara())
# print("Summa:", tilasto.summa())
# print("Keskiarvo:", tilasto.keskiarvo())

tilasto = Lukutilasto()
parittomat = Lukutilasto()
parilliset = Lukutilasto()

while True:
    luku=input("Anna lukuja:")
    if luku == str(-1):
        break
    else:
        if int(luku)%2==0:
            parilliset.lisaa_luku(luku)
        else:
            parittomat.lisaa_luku(luku)
            
        tilasto.lisaa_luku(luku)

print("Summa:", tilasto.summa())
print("Keskiarvo:", tilasto.keskiarvo())
print("Parillisten summa:", parilliset.summa())
print("Parittomien summa:", parittomat.summa())