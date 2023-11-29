# tee ratkaisu tänne
def nelio_oikein(sudoku: list, rivi_nro: int, sarake_nro: int):
    
    luvut = []
    for rivi in range(rivi_nro,int(rivi_nro +3)):
        for sarake in range(sarake_nro,int(sarake_nro+3)):
            if sudoku[rivi][sarake] > 0 and sudoku[rivi][sarake] in luvut:
                return False
            luvut.append(sudoku[rivi][sarake])
        
    return True

def rivi_oikein(taulukko,rivi):
    
    oikein=True

    for i in range (1,10):
        if taulukko[rivi].count(i) > 1:
            oikein = False

    return oikein

def sarake_oikein(sudoku: list, sarake_nro: int):
    
    luvut = []
    for rivi in sudoku:
        if rivi[sarake_nro] > 0 and rivi[sarake_nro] in luvut:
            return False
        luvut.append(rivi[sarake_nro])
    
    return True

def sudoku_oikein(sudoku: list):
   
    oikein=True
    neliot=[(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3),(6, 6)]
    
    for rivi in range(0,len(sudoku[0])):
        if rivi_oikein(sudoku,rivi) == False:
            oikein=False
    for sarake in range(0,len(sudoku[0])):
        if sarake_oikein(sudoku,sarake) == False:
            oikein=False
    for nelio in neliot:
        if nelio_oikein(sudoku,nelio[0],nelio[1]) == False:
            oikein=False

    return oikein



 
if __name__ == "__main__":   
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_oikein(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_oikein(sudoku2))