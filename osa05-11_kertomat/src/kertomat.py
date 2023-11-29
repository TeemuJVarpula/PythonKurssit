# tee ratkaisu tänne
def kertomat(n: int):
    sanakirja = {}

    for i in range (1,n+1):
        sanakirja[i]=1
        for j in range (1,i+1):
            sanakirja[i]=sanakirja[i]*j
    return sanakirja

if __name__ == "__main__":
    k = kertomat(5)
    print(k[1])
    print(k[3])
    print(k[5])