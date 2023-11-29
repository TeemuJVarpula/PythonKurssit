# Kirjoita ratkaisu tähän
lampotila = int(input("Anna lämpötila (F):"))
celsiukset = (lampotila -32)/1.8

print(f"{lampotila} fahrenheit-astetta on {celsiukset} celsius-astetta")

if celsiukset<0:
    print("Paleltaa!")