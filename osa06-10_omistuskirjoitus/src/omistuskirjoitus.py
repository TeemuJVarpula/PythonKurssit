# tee ratkaisu tänne


nimi=input("Kenelle teos omistetaan:")
tiedosto=input("Mihin kirjoitetaan:")

with open(tiedosto, "w") as tiedosto:
    tiedosto.write(f"Hei {nimi}, toivomme viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi")