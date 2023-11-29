# tee ratkaisu tänne

def lukukirja():
    luvut=["","yksi","kaksi","kolme","neljä","viisi","kuusi","seitsemän","kahdeksan","yhdeksän"]
    sanakirja={}
    laskuri=0
    
    for i in range (0,10):
        
        for j in range(0,10):
            numero=""
            if i==0 and j==0:
                numero="nolla"
            elif i==1 and j==0:
                numero="kymmenen"
            elif i==1 and j!=0:
                numero=luvut[j]+"toista"
            elif i>1:
                numero=luvut[i]+"kymmentä"
                numero=numero+luvut[j]
            else:
                numero=numero+luvut[j]

            sanakirja[laskuri]=numero
            laskuri +=1
    return sanakirja
        

if __name__ == "__main__":
    luvut = lukukirja()
    print(luvut[2])
    print(luvut[11])
    print(luvut[45])
    print(luvut[99])
    print(luvut[0])