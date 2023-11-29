# Kirjoita ratkaisu tähän
salasana=input("Salasana:")

while True:
    if (input("Toista salasana:") == salasana):
        break

    print("Ei ollut sama!")

print("Käyttäjätunnus luotu!")