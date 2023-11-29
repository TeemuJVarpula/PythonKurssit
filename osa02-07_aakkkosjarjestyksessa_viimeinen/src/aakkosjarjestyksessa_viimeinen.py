# Kirjoita ratkaisu tähän
sana = str(input("Anna 1. sana:"))
sana2 = str(input("Anna 2. sana:"))

if sana > sana2:
    print(f"{sana} on aakkosjärjestyksessä viimeinen.")
elif sana < sana2:
    print(f"{sana2} on aakkosjärjestyksessä viimeinen.")
else:
    print(f"Annoit saman sanan kahdesti.")