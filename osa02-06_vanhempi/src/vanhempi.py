# Kirjoita ratkaisu tähän
print(f"Henkilö 1:")
Nimi = input("Nimi:")
ika = int(input("Ika::"))
print(f"Henkilö 2:")
Nimi2 = input("Nimi:")
ika2 = int(input("Ika::"))

if ika > ika2:
    print(f"Vanhempi on {Nimi}")
elif ika < ika2:
    print(f"Vanhempi on {Nimi2}")
else:
    print(f"{Nimi} ja {Nimi2} ovat yhtä vanhoja")