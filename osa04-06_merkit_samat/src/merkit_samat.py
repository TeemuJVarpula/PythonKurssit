# tee ratkaisu tänne
def samat(sana,luku,luku2):
    
    if luku>=len(sana) or luku2>=len(sana):
        return False
    else:
        if sana[luku]==sana[luku2]:
            return True
        else:
            return False

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    #samat merkit o ja o
    print(samat("koodari", 1, 2)) # True

    # eri merkit k ja a
    print(samat("koodari", 0, 4)) # False

    # toinen indeksi ei ole merkkijonon sisällä
    print(samat("koodari", 0, 10)) # False

    print(samat("abc", 0, 3))