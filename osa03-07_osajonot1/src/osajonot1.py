# Kirjoita ratkaisu tähän
sana = input("Anna merkkijono:")
sana2=""
laskuri=0
laskuri2=0

while laskuri<len(sana)+1:
    while laskuri2<laskuri:
        sana2=sana2+sana[laskuri2]
        laskuri2 +=1
    
    laskuri2=0
    laskuri +=1
    print(sana2)
    sana2=""