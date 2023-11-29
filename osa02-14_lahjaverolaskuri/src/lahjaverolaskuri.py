# Kirjoita ratkaisu tähän
maara=int(input("Lahjan suuruus?"))

if maara < 5000:
    print("Ei veroa!")
elif maara < 25000:
    print(f"Vero: {(100 + (maara-5000) * 0.08)} euroa")
elif maara < 55000:
    print(f"Vero: {(1700 + (maara-25000) * 0.10)} euroa")
elif maara < 200000:
    print(f"Vero: {(4700 + (maara-55000) * 0.12)} euroa")
elif maara < 1000000:
    print(f"Vero: {(22100 + (maara-200000) * 0.15)} euroa")
else: #maara > 1000000
    print(f"Vero: {(142100 + (maara-1000000) * 0.17)} euroa")