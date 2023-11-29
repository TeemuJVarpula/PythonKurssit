# tee ratkaisu tänne

def pelaa_siirto(lauta: list, x: int, y: int, nappula: str):
    if 0 <= x <= 2 and 0 <= y <= 2:
        if lauta[y][x]=="":
            lauta[y][x]=nappula
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    lauta = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(pelaa_siirto(lauta, 2, 0, "X"))
    print(lauta)
    print(pelaa_siirto(lauta, 0, 0, "x"))
    print(lauta)