# Kirjoita ratkaisu tähän
luku=0
asti= int(input("Mihin asti:"))
arvo=1
laskettu=""
while luku<asti:
    luku=luku+arvo
    laskettu=laskettu+str(arvo)
    arvo+=1;
    if luku<asti:
        laskettu=laskettu+" + "

print(f"Laskettiin {laskettu} = {luku}")
