# Kirjoita ratkaisu tähän
luku=int(input("Anna luku:"))
kertoja=1
kerrottava=1

while kerrottava <= luku:
    while kertoja <= luku:
        print (f"{kerrottava} x {kertoja} = {kerrottava*kertoja}")
        kertoja +=1

    kerrottava +=1
    kertoja=1
