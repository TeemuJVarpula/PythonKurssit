# Kirjoita ratkaisu tähän
ika=int(input ("Kerro ikäsi?"))

if ika<0 or ika>100:
    print(f"Taitaa olla virhe")
elif 0<=ika<5:
    print(f"En usko, että osaat kirjoittaa...")
else:
    print(f"Ok, olet siis {ika}-vuotias")