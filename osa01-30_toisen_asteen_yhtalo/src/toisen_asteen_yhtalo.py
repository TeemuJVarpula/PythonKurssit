# Kirjoita ratkaisu tähän
# Otetaan käyttöön neliöjuuri math-moduulista
from math import sqrt

# Huomaa, että neliöjuuren voi laskea myös potenssin avulla:
# sqrt(9) on sama asia kuin 9 ** 0.5

a = float(input("Anna a:"))
b = float(input("Anna b:"))
c = float(input("Anna c:"))

juri  = a/b
juuri  = ((-b + sqrt((b**2) - (4*a*c))) / (2*a))
juuri2 = ((-b - sqrt((b**2) - (4*a*c))) / (2*a))

print(f"Juuret ovat {juuri} ja {juuri2}")