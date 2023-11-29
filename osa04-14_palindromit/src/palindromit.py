# tee ratkaisu tänne
# huomaa, että tällä kertaa pääohjelmaa ei tule kirjoittaa lohkon
# if __name__ == "__main__":
# sisälle!

def palindromi(sana):
    palindromitesti=True
    for i in range(0,int(len(sana))):
        if sana[i]!=sana[int(len(sana))-(i+1)]:
            palindromitesti= False
    
    if palindromitesti == False:
        return False
    else:
        return True

while True:
    mjono = input("Anna palindromi: ")
  
    if palindromi(mjono) == True:
        print(f"{mjono} on palindromi!")
        break
    else:
        print(f"ei ollut palindromi")   
       

