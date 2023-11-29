# Kirjoita ratkaisu tähän
opiskelijaMaara = int(input("Montako opiskelijaa?"))
ryhmaKoko = int(input("Mikä on ryhmän koko?"))

ryhmaLkm = int(opiskelijaMaara/ryhmaKoko)
jakojaannos = float(opiskelijaMaara%ryhmaKoko)

if jakojaannos > 0:
  print(f"Ryhmien määrä: {ryhmaLkm+1}")
else:
  print(f"Ryhmien määrä: {ryhmaLkm}")
