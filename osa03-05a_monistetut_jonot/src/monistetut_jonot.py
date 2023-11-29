# Kirjoita ratkaisu tähän
merkkijono = input("Anna merkkijono:")
lkm = int(input("Anna määrä:"))
merkit=""

while lkm != 0:
    merkit=merkit+merkkijono
    lkm-=1

print (merkit)