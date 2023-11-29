# tee ratkaisu tänne
 

def hypotenuusa(k1: float, k2: float):
    hypotenuusa=0

    hypotenuusa= sqrt(k1**2+k2**2)

    return hypotenuusa

if __name__ == "__main__":
    print(hypotenuusa(3,4)) # 5.0
    print(hypotenuusa(5,12)) # 13.0
    print(hypotenuusa(1,1)) # 1.4142135623730951