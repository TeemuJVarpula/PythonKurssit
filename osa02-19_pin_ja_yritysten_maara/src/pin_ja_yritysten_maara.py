# Kirjoita ratkaisu tähän
pin=4321
yrityksia=0

while True:
    yrityksia +=1

    if (int(input("PIN-koodi:")) == pin):
        
        break

    print("Väärin")
    
if yrityksia==1:
    print("Oikein, tarvitsit vain yhden yrityksen!")
else:
    print(f"Oikein, tarvitsit {yrityksia} yritystä")
