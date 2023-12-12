# TEE RATKAISUSI TÄHÄN:
from datetime import date,timedelta

class Paivays:
    def __init__(self,paiva:int,kuukausi:int,vuosi:int):
        self.__vuosi = vuosi
        self.__kuukausi = kuukausi
        self.__paiva = paiva
        
    def __str__(self):
        return f"{self.__paiva}.{self.__kuukausi}.{self.__vuosi}"
    
    def __eq__(self, toinen):
        
        if self.__vuosi==toinen.__vuosi and self.__kuukausi==toinen.__kuukausi and self.__paiva==toinen.__paiva:
            return True
        else:
            return False
            
    def __lt__(self, toinen):
        
        if self.__vuosi<toinen.__vuosi:
            return True
        elif self.__vuosi==toinen.__vuosi and self.__kuukausi<toinen.__kuukausi:
            return True
        elif self.__vuosi==toinen.__vuosi and self.__kuukausi==toinen.__kuukausi and self.__paiva<toinen.__paiva:
            return True
        else:
            return False
            
    def __gt__(self, toinen):
        
        if self.__vuosi>toinen.__vuosi:
            return True
        elif self.__vuosi==toinen.__vuosi and self.__kuukausi>toinen.__kuukausi:
            return True
        elif self.__vuosi==toinen.__vuosi and self.__kuukausi==toinen.__kuukausi and self.__paiva>toinen.__paiva:
            return True
        else:
            return False
    
    def __ne__(self, toinen):
        if self.__vuosi!=toinen.__vuosi or self.__kuukausi!=toinen.__kuukausi or self.__paiva!=toinen.__paiva:
            return True
        else:
            return False

    def __add__(self, toinen):
        
        uusiaika=Paivays(self.__paiva,self.__kuukausi,self.__vuosi)

        if toinen // 360 > 0:
            maara_y = toinen // 360 
            uusiaika.__vuosi += maara_y
            toinen=toinen-maara_y*360
        
        if toinen // 30  > 0:
            maara_kk = toinen // 30 
            uusiaika.__kuukausi += maara_kk
            toinen=toinen-maara_kk*30
    
        uusiaika.__paiva = uusiaika.__paiva + toinen
        
        if uusiaika.__paiva > 30:
            uusiaika.__paiva=uusiaika.__paiva-30
            uusiaika.__kuukausi +=1
        
        if uusiaika.__kuukausi >12:
            uusiaika.__kuukausi=uusiaika.__kuukausi-12
            uusiaika.__vuosi +=1
    
        return uusiaika
    
    def __sub__(self, toinen):
        maara_y=0
        maara_m=0
        maara_d=0
        
        if self.__gt__(toinen):
            if self.__vuosi-toinen.__vuosi>0:
                maara_y=self.__vuosi-toinen.__vuosi
            
            if self.__kuukausi-toinen.__kuukausi>0:
                maara_m=self.__kuukausi-toinen.__kuukausi
            else:
                maara_m=12+self.__kuukausi-toinen.__kuukausi
                maara_y -=1
            
            if self.__paiva-toinen.__paiva>0:
                maara_d=self.__paiva-toinen.__paiva
            else:
                maara_d=30+self.__paiva-toinen.__paiva
                maara_m -=1
        else:
            if toinen.__vuosi-self.__vuosi>0:
                maara_y=toinen.__vuosi-self.__vuosi
            
            if toinen.__kuukausi-self.__kuukausi>0:
                maara_m=toinen.__kuukausi-self.__kuukausi
            else:
                maara_m=12+toinen.__kuukausi-self.__kuukausi
                maara_y -=1
            
            if toinen.__paiva-self.__paiva>0:
                maara_d=toinen.__paiva-self.__paiva
            else:
                maara_d=30+toinen.__paiva-self.__paiva
                maara_m -=1       
            
        return maara_y*12*30+maara_m*30+maara_d
        
if __name__ == "__main__":
    p1 = Paivays(4, 10, 2020)
    # p2 = Paivays(28, 12, 1985)
    # p3 = Paivays(28, 12, 1985)
    # print(p1)
    # print(p2)
    # print(p1 == p2)
    # print(p1 != p2)
    # print(p1 == p3)
    # print(p1 < p2)
    # print(p1 > p2)
    
    
    # p1 = Paivays(4, 10, 2020)
    # p2 = Paivays(28, 12, 1985)
    # p3 = p1 + 3
    # p4 = p2 + 400
    # print(p1)
    # print(p2)
    # print(p3)
    # print(p4)
    
    # pvm = Paivays(1, 5, 1878)
    # print(pvm + 30)
    
    p1 = Paivays(4, 10, 2020)
    p2 = Paivays(2, 11, 2020)
    p3 = Paivays(28, 12, 1985)

    print(p2-p1)
    print(p1-p2)
    print(p1-p3)
