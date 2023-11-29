# tee ratkaisu tänne
import copy
def tulosta(sudoku:list):

    for rivi in range (0,len(sudoku)):
        mjono=""

        if rivi%3==0:
                print()

        for sarake in range (0,len(sudoku[rivi])):
            if sarake!=0 and sarake%3==0:
                mjono=mjono + " "
                
            if sudoku[rivi][sarake]==0:
                mjono=mjono + "_ "
            else:
                mjono=mjono + str(sudoku[rivi][sarake]) + " "
            
        print(mjono)
    print()

def kopioi_ja_lisaa(sudoku2: list, rivi_nro: int, sarake_nro: int, luku:int):
    
    kopio = copy.deepcopy(sudoku2)  # for r in sudoku2: kopio.append(r[:])
    print(id(kopio), id(sudoku2))
    kopio[rivi_nro][sarake_nro]=luku
    return kopio

if __name__ == "__main__":

    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    kopio = kopioi_ja_lisaa(sudoku, 0, 0, 4)
    print("Alkuperäinen:")
    tulosta(sudoku)
    print()
    print("Kopio:")
    tulosta(kopio)