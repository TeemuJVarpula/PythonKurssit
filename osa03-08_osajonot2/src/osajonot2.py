# Kirjoita ratkaisu tähän
sana = input("Anna merkkijono:")
sana2=""
laskuri=0
laskuri2=1

while laskuri<len(sana)+1:
    laskuri2=len(sana)-laskuri

    while laskuri2<len(sana):
        sana2=sana2+sana[laskuri2]
        laskuri2 +=1

    laskuri +=1
    print(sana2)
    sana2=""