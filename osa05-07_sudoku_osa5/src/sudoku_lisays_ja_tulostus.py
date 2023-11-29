# tee ratkaisu tänne
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

def lisays(sudoku: list, rivi_nro: int, sarake_nro: int, luku:int):
    
    sudoku[rivi_nro][sarake_nro]=luku


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

    tulosta(sudoku)
    lisays(sudoku, 0, 0, 2)
    lisays(sudoku, 1, 2, 7)
    lisays(sudoku, 5, 7, 3)
    print()
    print("Kolme numeroa lisätty:")
    print()
    tulosta(sudoku)