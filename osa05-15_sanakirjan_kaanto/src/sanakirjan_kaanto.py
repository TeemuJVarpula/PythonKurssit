# tee ratkaisu tänne
def kaanna(sanakirja: dict):
    apusanakirja={}

    for sanat in sanakirja:
    
        if sanakirja[sanat] not in apusanakirja:
            apusanakirja[sanakirja[sanat]] = sanat
        else:      
            apusanakirja[sanakirja[sanat]].append(sanat)

    sanakirja.clear()
    
    for sanat in apusanakirja:
        sanakirja[sanat] = apusanakirja[sanat]
    
if __name__ == "__main__":

    s = {1: "eka", 2: "toka", 3: "kolmas", 4: "neljas"}
    kaanna(s)
    print(s)
