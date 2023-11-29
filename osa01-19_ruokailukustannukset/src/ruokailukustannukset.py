# Kirjoita ratkaisu tähän
kerrat=int(input("Montako kertaa viikossa syöt Unicafessa?"))
hinta=float(input("Unicafe-lounaan hinta?"))
ostokset=float(input("Paljonko käytät viikossa ruokaostoksiin?"))

pkulut=float(((kerrat * hinta) + ostokset) / 7)
vkulut=(kerrat * hinta) + ostokset

print("\n" + "Kustannukset keskimäärin:")
print(f"Päivässä {pkulut} euroa")
print(f"Viikossa {vkulut} euroa")