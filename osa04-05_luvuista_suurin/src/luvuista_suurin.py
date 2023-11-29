# tee ratkaisu tänne
def luvuista_suurin(luku,luku2,luku3):
    suurin=[luku,luku2,luku3]
    suurin.sort() 
    
    return suurin[-1] 



    return suurin
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    suurin = luvuista_suurin(5, 4, 8)
    print(suurin)