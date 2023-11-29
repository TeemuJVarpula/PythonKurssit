# tee ratkaisu tänne
import string

def jaa_merkkeihin(merkkijono: str):
    osat=["","",""]

    for merkki in merkkijono:
        tarkastelu=0
        if merkki in string.ascii_letters:
            osat[0]=osat[0]+merkki
            tarkastelu +=1
        
        if merkki in string.punctuation:
            osat[1]=osat[1]+merkki
            tarkastelu +=1

        if tarkastelu==0:
            osat[2]=osat[2]+merkki
    
    return (osat[0],osat[1],osat[2])

if __name__ == "__main__":
    osat = jaa_merkkeihin("Tämä on testi!!! Toimiiko, mitä?")
    print(osat[0])
    print(osat[1])
    print(osat[2])