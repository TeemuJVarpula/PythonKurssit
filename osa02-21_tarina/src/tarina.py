# Kirjoita ratkaisu tähän
sana=""
edellinen=""
loru=""

while True:
    sana=input("Anna sana:")

    if sana == edellinen:
        break
    elif sana == "loppu":
        break

    edellinen=sana
    loru +=( sana + " " )

print(loru)