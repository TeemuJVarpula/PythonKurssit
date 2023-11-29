# Kirjoita ratkaisu tähän

lista=[]

while True:
    print(f"Lista on nyt {lista} ")
    valinta=input("(l)isää, (p)oista vai e(x)it:")

    if valinta == "x":
        break
    elif valinta=="p" and len(lista)>0:
        lista.pop(len(lista)-1)
    elif valinta=="l":
        lista.append(len(lista)+1)
    else:
        continue


print("Moi!")