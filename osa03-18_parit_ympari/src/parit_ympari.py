# Kirjoita ratkaisu tähän
luku = int(input("Anna luku:"))
laskuri=1

while laskuri <= luku:

    if laskuri%2 != 0 and laskuri+1<=luku:
        print(laskuri+1)
    elif laskuri%2 != 0:
        print(laskuri)
    else:
        print(laskuri-1)
    laskuri +=1 

      