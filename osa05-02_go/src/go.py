# tee ratkaisu tänne

def kumpi_voitti(pelilauta: list):

    pelaaja1=0
    pelaaja2=0

    for rivi in pelilauta:
        for ruutu in rivi:
            if int(ruutu) == 1:
                pelaaja1 +=1
            elif int(ruutu) == 2:
                pelaaja2 +=1   
                
    if pelaaja1>pelaaja2:
        return 1
    elif pelaaja2>pelaaja1:
        return 2
    else:
        return 0
    
if __name__ == "__main__":

    voittaja=kumpi_voitti([[1]])
    print(voittaja)