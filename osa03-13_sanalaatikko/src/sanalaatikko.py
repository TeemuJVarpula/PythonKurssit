# Kirjoita ratkaisu tähän
mjono = input ("Sana:")
tahdet="**"
sana="* "
laskuri=2
laskuri2=0

while laskuri < 29:
    tahdet = "*" + tahdet

    
    if laskuri < int((30-len(mjono))/2) or laskuri2>=len(mjono):
        sana=sana + " "
    else:
        sana=sana + mjono[laskuri2]
        laskuri2 +=1
    

    laskuri +=1

tahdet=tahdet +"*"
sana=sana+"*"

print (tahdet)    
print (sana)
print (tahdet)