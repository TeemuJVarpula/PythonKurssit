# tee ratkaisu tänne
def histogrammi(mjono):
    sanakirja={}

    for kirjain in mjono:
        
        if kirjain not in sanakirja:
            sanakirja[kirjain] = ""

        sanakirja[kirjain]=str(sanakirja[kirjain])+"*"

    for sana in sanakirja:
        print(f"{sana} {sanakirja[sana]}")



if __name__ == "__main__":
     histogrammi("abba")
     histogrammi("saippuakauppias")