# Kirjoita ratkaisu tähän
jono = input("Anna jono 1:")
jono2 = input("Anna jono 2:")

if len(jono) > len(jono2):
    print(f"{jono} on pidempi")
elif len(jono) < len(jono2):
    print(f"{jono2} on pidempi")
else:
    print("Jonot ovat yhtä pitkät")