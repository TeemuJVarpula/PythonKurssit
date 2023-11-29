from math import sqrt
# Kirjoita ratkaisu tähän
while True:
    
    luku = int(input("Syötä luku: "))
    if luku == 0:
        print("Lopetetaan...")
        break
    elif luku < 0:
        print("Epäkelpo luku")
        continue
    print(float(sqrt(luku)))