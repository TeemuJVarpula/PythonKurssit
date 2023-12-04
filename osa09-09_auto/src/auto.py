# TEE RATKAISUSI TÄHÄN:
class Auto:
    def __init__(self):
        self.__tankissa=0
        self.__ajettu=0
        
    
    def tankkaa(self):
        self.__tankissa=60
    
    def aja(self,km:int):
        if self.__tankissa>km:
            self.__tankissa=self.__tankissa-km
            self.__ajettu=self.__ajettu+km
        else: 
            self.__ajettu=self.__ajettu+self.__tankissa
            self.__tankissa=0
        
    def __str__(self):
        return f"Auto: ajettu {self.__ajettu} km, bensaa {self.__tankissa} litraa"
if __name__ == "__main__":
    auto = Auto()
    print(auto)
    auto.tankkaa()
    print(auto)
    auto.aja(20)
    print(auto)
    auto.aja(50)
    print(auto)
    auto.aja(10)
    print(auto)
    auto.tankkaa()
    auto.tankkaa()
    print(auto)