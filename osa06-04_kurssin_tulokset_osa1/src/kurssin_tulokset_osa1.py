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
    

    
opiskelijat=[]
numerot=[]

if True:
    opiskelijatiedot = input("Opiskelijatiedot: ")
    tehtavatiedot = input("Tehtävätiedot: ")
else:
    opiskelijatiedot = "opiskelijat1.csv"
    tehtavatiedot = "tehtavat1.csv"
print()

opiskelijat=lue_tiedosto(opiskelijatiedot)


numerot=lue_tiedosto(tehtavatiedot)

for i in range (0,len(opiskelijat)): #check srttudent
    summa=0
    for j in range (0,len(numerot)): #find student and count sum
        if numerot[j][0][1]==opiskelijat[i][0][1]:
            for k in range(1,len(numerot[j])):
                summa=summa+int(numerot[j][k][1])
            break

    print(f"{opiskelijat[i][1][1]} {opiskelijat[i][2][1]} {summa}")