# Kirjoita ratkaisu tähän
tunnit    = float(input("Tuntipalkka:"))
tyotunnit = int(input("Työtunnit:"))
paiva     = input("Viikonpäivä:")

laskettu = tunnit*tyotunnit

if paiva == "sunnuntai":
  laskettu=laskettu*2

print(f"Palkka {laskettu} euroa")