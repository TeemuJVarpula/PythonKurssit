# Kirjoita ratkaisu tähän

leveys = int(input("Leveys:"))
korkeus = int(input("Korkeus:"))
maara = 0
merkit=""
while maara < leveys:
    merkit = merkit + "#"
    maara +=1

maara =0
while maara < korkeus:
    print (merkit)
    maara +=1