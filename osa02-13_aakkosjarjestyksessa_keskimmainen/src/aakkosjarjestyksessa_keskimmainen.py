# Kirjoita ratkaisu tähän
kirjain=[]
kirjain.append(input("Anna 1. kirjain:"))
kirjain.append(input("Anna 2. kirjain:"))
kirjain.append(input("Anna 3. kirjain:"))

kirjain.sort()

print(f"Keskimmäinen kirjain on {kirjain[1]}")