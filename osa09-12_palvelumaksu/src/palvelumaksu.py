# TEE RATKAISUSI TÄHÄN:

class Pankkitili:
    def __init__(self,omistaja:str,tili:str,cur_saldo:float):
        self.__omistaja = omistaja
        self.__tili = tili
        self.__cur_saldo = float(cur_saldo)
    
    def talleta(self,summa:float):
        if summa>=0:
            self.saldo=float(self.__cur_saldo+summa)

    def nosta(self,summa:float):
        if float(self.__cur_saldo)>=summa:
            self.saldo=float(self.__cur_saldo-summa)
            
    def __palvelumaksu(self):
        self.__cur_saldo=float(self.__cur_saldo-self.__cur_saldo*0.01)
        
    def __str__(self):
        return f"{self.__omistaja} {self.__tili} {self.__cur_saldo}"

    @property
    def saldo(self):
        return self.__cur_saldo
    
    @saldo.setter
    def saldo(self,summa:float):
        if summa>0:
            self.__cur_saldo=summa
            
        self.__palvelumaksu()
        None
    
    
    
if __name__ == "__main__":    
    tili = Pankkitili("Raimo Rahakas", "12345-6789", 1000)
    tili.nosta(100)
    print(tili.saldo)
    tili.talleta(100)
    print(tili.saldo)
    
    