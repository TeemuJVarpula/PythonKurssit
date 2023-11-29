# tee ratkaisu tänne
def risunelio(maara):
    neliot=""
    for i in range(0,maara):
        neliot=neliot+"#"
        
    for i in range(0,maara):    
        print(neliot)

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risunelio(5)