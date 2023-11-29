# Kirjoita ratkaisu tähän

sana = input("Sana:")
merkki = input("Merkki:")
merkit=""
kohta = sana.find(merkki)
while kohta<len(sana) and kohta>=0:
    if kohta < sana.find(merkki)+3:
        merkit=merkit+sana[kohta]
    kohta+=1

if len(merkit)==3:
    print(merkit)