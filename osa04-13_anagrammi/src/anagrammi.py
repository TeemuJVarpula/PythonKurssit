# tee ratkaisu tänne

def anagrammi(sana,sana2):

    if sorted(sana)==sorted(sana2):
        return True
    else:  
        return False

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    print(anagrammi("talo", "tola")) # True
    print(anagrammi("talo", "lato")) # True
    print(anagrammi("talo", "olat")) # True
    print(anagrammi("tammi", "mitta")) # False
    print(anagrammi("python", "java")) # False