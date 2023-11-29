# tee ratkaisu tänne
# tee ratkaisu tänne
numerokirja={}

while(True):

    syote=int(input("komento (1 hae, 2 lisää, 3 lopeta):"))
    if syote==3:
        print("lopetetaan...")
        break

    elif syote==2:
        nimi=str(input("nimi:"))
        numero=input("numero:") 

        if nimi not in numerokirja:
            numerokirja[nimi] = [numero]
        else:      
            numerokirja[nimi].append(numero)

        print("ok!") 
 
    elif syote==1:
        nimi=str(input("nimi:"))

        if str(nimi) not in numerokirja:
            print("ei numeroa")
        else:
            for arvo in numerokirja[nimi]:
                print(arvo)
            
           