# Kirjoita ratkaisu tähän
lause=input("Anna lause:")
kohta = 0

print(lause[kohta])

while True:
    kohta = lause.find(" ")

    if kohta>=0:
        print(lause[kohta+1])
    else:
        break

    lause=lause[kohta+1:]