# tee ratkaisu tänne

def pisin(mjonot):
    pisinsana=mjonot[0]

    for i in range(1,len(mjonot)):
        if len(pisinsana)<len(mjonot[i]):
            pisinsana=mjonot[i]
    
    return pisinsana
        

if __name__ == "__main__":
    jonot = ["moi", "moikka", "heip", "hellurei", "terve"]
    print(pisin(jonot))