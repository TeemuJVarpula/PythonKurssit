# Kirjoita ratkaisu tähän
luku = int(input("Anna luku:"))
kertoma=0
laskuri=0

while luku>0:
    kertoma=luku
    laskuri=luku-1

    while laskuri>0:
        kertoma= kertoma*laskuri
        laskuri -=1

    print(f"Luvun {luku} kertoma on {kertoma}")
    luku = int(input("Anna luku:"))

print("Kiitos ja moi!")