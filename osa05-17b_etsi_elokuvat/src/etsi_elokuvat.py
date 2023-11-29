# tee ratkaisu tänne
def lisaa_elokuva(rekisteri: list, nimi: str, ohjaaja: str, vuosi: int, pituus: int):

    rekisteri.append({"nimi":nimi,"ohjaaja":ohjaaja, "vuosi": vuosi, "pituus": pituus})

def etsi_elokuvat(rekisteri: list, hakusana: str):

    hakutulos=[]

    for elokuva in rekisteri:
        if (elokuva["nimi"]).upper().find(hakusana.upper()) != -1:
            hakutulos.append(elokuva)

        # if hakusana.lower() in elokuva["nimi"].lower():
        #     loydetyt.append(elokuva)
 


    return hakutulos

if __name__ == "__main__":
    rekisteri = [{"nimi": "Pythonin viemää", "ohjaaja": "Pekka Python", "vuosi": 2017, "pituus": 116},
    {"nimi": "Python lentokoneessa", "ohjaaja": "Renny Pythonen", "vuosi": 2001, "pituus": 94},
    {"nimi": "Koodaajien yö", "ohjaaja": "M. Night Python", "vuosi": 2011, "pituus": 101}]

    lista = etsi_elokuvat(rekisteri, "python")
    print(lista)