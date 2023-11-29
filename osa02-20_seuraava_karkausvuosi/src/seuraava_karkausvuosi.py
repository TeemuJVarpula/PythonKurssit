# Kirjoita ratkaisu tähän
vuosi=int(input("Vuosi:"))
karkausvuosi=vuosi

while True:
    karkausvuosi +=1

    if karkausvuosi%4==0:
        if karkausvuosi%100!=0:
            break
        elif karkausvuosi%100==0 and karkausvuosi%400==0:
            break      

print(f"Vuotta {vuosi} seuraava karkausvuosi on {karkausvuosi}")
