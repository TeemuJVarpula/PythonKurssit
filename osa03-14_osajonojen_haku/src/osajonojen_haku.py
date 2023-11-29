# Kirjoita ratkaisu tähän
sana = input("Sana: ")
merkki = input("Merkki:")
kohta = 0

while True:
    if len(sana) == 0:
        break

    kohta = int(sana.find(merkki))

    if kohta == -1:
        break
    elif (kohta+3)<len(sana)+1:
        print(sana[kohta:kohta+3])
            
    sana = sana[kohta+1:]

