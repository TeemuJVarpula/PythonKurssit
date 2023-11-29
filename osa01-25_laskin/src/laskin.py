# Kirjoita ratkaisu tähän
luku=int(input("Luku1:"))
luku2=int(input("Luku2:"))
komento=str(input("Komento:"))

if komento == "summa":
  print(f"\n{luku} + {luku2} = {luku+luku2}")
if komento == "tulo":
   print(f"\n{luku} * {luku2} = {luku*luku2}")
if komento == "erotus":
   print(f"\n{luku} - {luku2} = {luku-luku2}")