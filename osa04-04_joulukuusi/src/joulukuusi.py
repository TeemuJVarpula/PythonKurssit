# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
def joulukuusi(rivit):
   
    print("joulukuusi!")
    print((rivit-1)*" " + "*" + (rivit-1)*" ")
    for i in range(1,rivit):
        #for j in range(1,rivit,2):
        rivi=(rivit-i-1)*" " + (2*i+1)*"*" + (rivit-i-1)*" "
        print(rivi)

    print((rivit-1)*" " + "*" + (rivit-1)*" ")

if __name__ == "__main__":
    joulukuusi(5)