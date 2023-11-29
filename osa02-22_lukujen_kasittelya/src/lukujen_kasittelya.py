# Kirjoita ratkaisu tähän
lkm=0
summa=0
posit=0
negat=0

print("Syötä kokonaislukuja, 0 lopettaa:")
while True:
    luku=int(input("Luku:"))

    if luku==0:
        break
    elif luku < 0:
        negat +=1
    else:
        posit +=1

    summa +=luku
    lkm   +=1


print(f"Lukuja yhteensä {lkm}")
print(f"Lukujen summa {summa}")
print(f"Lukujen keskiarvo {summa/lkm}")

print(f"Positiivisia {posit}")
print(f"Negatiivisia {negat}")