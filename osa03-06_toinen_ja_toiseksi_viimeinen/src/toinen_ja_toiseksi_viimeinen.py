# Kirjoita ratkaisu tähän
sana = input("Anna sana:")

if sana[-2] == sana[1]:
    print(f"Toinen ja toiseksi viimeinen kirjain on {sana[1]}")
else:
    print("Toinen ja toiseksi viimeinen kirjain eroavat")