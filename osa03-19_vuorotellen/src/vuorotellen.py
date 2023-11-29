# Kirjoita ratkaisu tähän
luku = int(input("Anna luku:"))
laskuri=1
laskuri2=luku

while laskuri<(luku/2+1):
    if laskuri <= luku/2:
        print(laskuri)
        print(laskuri2)
        laskuri +=1
        laskuri2 -=1
    else: 
        print(laskuri)
        break;
