# Kirjoita ratkaisu tähän

sanat=[]
sana=""
laskuri=1

while True:
    sana = input("sana: ")
    if sanat.count(sana) > 0:
        break
    else:
        sanat.append(sana)
    laskuri +=1

print(f"Annoit {laskuri-1} eri sanaa")