# TEE RATKAISUSI TÄHÄN:
class Raha:
    def __init__(self, eurot: int, sentit: int):
        self.__eurot = eurot
        self.__sentit = sentit

    def __str__(self):
        return f"{self.__eurot}.{self.__sentit:02d} eur"

    def __eq__(self, toinen):
        
        if self.__eurot==toinen.__eurot and self.__sentit==toinen.__sentit:
            return True
        else:
            return False
            
    def __lt__(self, toinen):
        
        if self.__eurot<toinen.__eurot:
            return True
        elif self.__eurot==toinen.__eurot and self.__sentit<toinen.__sentit:
            return True
        else:
            return False
            
    def __gt__(self, toinen):
        
        if self.__eurot>toinen.__eurot:
            return True
        elif self.__eurot==toinen.__eurot and self.__sentit>toinen.__sentit:
            return True
        else:
            return False
    
    def __ne__(self, toinen):
        if self.__eurot!=toinen.__eurot or self.__sentit!=toinen.__sentit:
            return True
        else:
            return False
    
    def __add__(self, toinen):
        
        u_eurot = self.__eurot+toinen.__eurot
        u_sentit = self.__sentit+toinen.__sentit
        
        if u_sentit>=100:
            u_sentit=u_sentit-100
            u_eurot +=1
            
        return Raha(u_eurot, u_sentit)
    
    def __sub__(self, toinen):
                
        u_eurot = self.__eurot-toinen.__eurot
        u_sentit = self.__sentit-toinen.__sentit
        
        if u_sentit<0:
            u_eurot -=1
            u_sentit =u_sentit+100
        
        if u_eurot>=0 and u_sentit >= 0:
            return Raha(u_eurot, u_sentit)
        else:
            raise ValueError("negatiivinen tulos ei sallittu")
    
if __name__ == "__main__":
    # e1 = Raha(4, 10)
    # e2 = Raha(2, 5)  # kaksi euroa ja viisi senttiä
    # print(e1)
    # print(e2)
    
    
    # e1 = Raha(4, 10)
    # e2 = Raha(2, 5)
    # e3 = Raha(4, 10)
    # print(e1)
    # print(e2)
    # print(e3)
    # print(e1 == e2)
    # print(e1 == e3)
    
    e1 = Raha(4, 10)
    e2 = Raha(2, 5)
    
    print(e1 != e2)
    print(e1 < e2)
    print(e1 > e2)
    
    # e1 = Raha(4, 5)
    # e2 = Raha(2, 95)

    # e3 = e1 + e2
    # e4 = e1 - e2

    # print(e3)
    # print(e4)

    # e5 = e2-e1
    
    # e1 = Raha(4, 5)
    # print(e1)
    # e1.eurot = 1000
    # print(e1)
    
    test_cases = [((1,0), (2,0)), ((2,50),(3,50)), ((4,5),(4,50)), ((15,95),(15,96)),
        ((2,0), (1,0)), ((4,50), (4,5)), ((3,95),(3,95)), ((1110,10),(1110,1))]
    for test_case in test_cases:
        tc1,tc2 = test_case
        raha1 = Raha(tc1[0], tc1[1])
        raha2 = Raha(tc2[0], tc2[1])

        corr = tc1 < tc2
        val = (raha1 < raha2)
        stmt = "raha1 < raha2"
        met_name = "__lt__"

    