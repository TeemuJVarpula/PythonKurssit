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

        numerokirja[nimi] = numero 

        print("ok!") 
 
    elif syote==1:
        nimi=str(input("nimi:"))

        if str(nimi) not in numerokirja:
            print("ei numeroa")
        else: 
            print(numerokirja[nimi]) 