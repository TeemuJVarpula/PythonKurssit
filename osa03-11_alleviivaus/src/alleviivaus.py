# Kirjoita ratkaisu tähän

while True:
    mjono = input("Anna merkkijono:")
    maara = len(mjono)
    viiva = ""

    if len(mjono) == 0:
        break

    while maara > 0:
        viiva = viiva + "-"
        maara -=1

    print (mjono)
    print (viiva)