# Kirjoita ratkaisu tähän
mjono = input("Anna merkkijono: ")
osajono = input("Anna osajono:")
loydetty=-1
kohta=0

while True:
    if len(mjono) == 0:
        break
    
    kohta=int(mjono.find(osajono))

    if kohta>=0 and loydetty<0:
        loydetty=mjono.find(osajono)
    elif kohta>=0 and loydetty>=0:
        kohta=mjono.find(osajono)+len(osajono)+loydetty
        print(f"Osajonon toinen esiintymä on kohdassa {kohta}.")
        break
    elif loydetty>=0:
        print(f"Osajono ei esiinny merkkijonossa kahdesti.")
        break
    else:
        print(f"Osajono ei esiinny merkkijonossa kahdesti.")
        break

    mjono = mjono[kohta+len(osajono):]
