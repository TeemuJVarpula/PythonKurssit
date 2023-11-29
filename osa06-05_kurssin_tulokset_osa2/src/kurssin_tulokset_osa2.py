# tee ratkaisu tänne
def lue_tiedosto(tiedostonimi):
    with open(tiedostonimi) as tiedosto:
        taulukko=[]
        otsikot=[]
        rivilaskuri=0

        
        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            sisalto=rivi.split(";")
            sarake=0

            if rivilaskuri!=0:
                taulukko.append([])
            
            for luku in sisalto:
                
                if rivilaskuri==0:
                    otsikot.append(luku)
                else:
                    
                    taulukko[(rivilaskuri-1)].append((otsikot[sarake],luku))
                    
                    sarake +=1

            

            rivilaskuri +=1

        return taulukko

def laskepisteet(numerot,kokeet,id):
    harjoitukset=0
    kokeet=0
    tulos=0
    for j in range (0,len(numerot)): #find student and count sum
        if numerot[j][0][1]==id:
            for k in range(1,len(numerot[j])):
                harjoitukset=harjoitukset+int(numerot[j][k][1])
            break

    for l in range (0,len(koepisteet)): #find student and count sum
        if koepisteet[l][0][1]==id:
            for m in range(1,len(koepisteet[l])):
                #print(koepisteet[l][m][1])
                kokeet=kokeet+int(koepisteet[l][m][1])
            break
    
    tulos=int(harjoitukset*10//40+kokeet)

    if tulos>=28:
        return(5)
    elif tulos>=24:
        return(4)
    elif tulos>=21:
        return(3)
    elif tulos>=18:
        return(2)
    elif tulos>=15:
        return(1)
    else:
        return(0)     




opiskelijat=[]
numerot=[]

if True:
    opiskelijatiedot = input("Opiskelijatiedot: ")
    tehtavatiedot = input("Tehtävätiedot: ")
    koepisteet = input("Koepisteet: ")
else:
    opiskelijatiedot = "opiskelijat1.csv"
    tehtavatiedot = "tehtavat1.csv"
    koepisteet = "koepisteet1.csv"
print()

opiskelijat=lue_tiedosto(opiskelijatiedot)
numerot=lue_tiedosto(tehtavatiedot)
koepisteet=lue_tiedosto(koepisteet)

for i in range (0,len(opiskelijat)): #check srttudent
    summa=laskepisteet(numerot,koepisteet,opiskelijat[i][0][1])

    print(f"{opiskelijat[i][1][1]} {opiskelijat[i][2][1]} {summa}")