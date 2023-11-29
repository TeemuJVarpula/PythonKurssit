# tee ratkaisu tähän
def tulosta_monesti(sana,maara):
    for i in range(0,maara):
        print(sana)
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    tulosta_monesti("python", 5)