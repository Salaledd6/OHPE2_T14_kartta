kartta = [[0,0,0,0,0,0,0,0,0,0], 
          [0,0,0,0,0,0,0,0,0,0], 
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0]]

class Merkki:
    def __init__(self, x, y, merkki):
        self.x = x
        self.y = y
        self.merkki = merkki
        kartta[y][x] = self # sijoitetaan olio itse (ts. osoite siihen) matriisiin

    def liiku_oikea(self):
        if self.x<9: 
            kartta[self.y][self.x] = 0
            self.x += 1
            kartta[self.y][self.x] = self

    def liiku_vasen(self):
        if self.x>0: 
            kartta[self.y][self.x] = 0
            self.x -= 1
            kartta[self.y][self.x] = self

    def liiku_ylos(self):
        if self.y>0: 
            kartta[self.y][self.x] = 0
            self.y -= 1
            kartta[self.y][self.x] = self

    def liiku_alas(self):
        if self.y<9: 
            kartta[self.y][self.x] = 0
            self.y += 1
            kartta[self.y][self.x] = self

    def __str__(self): #tulostetaan printissä merkki olion osoitteen sijasta
        return self.merkki
    
def main():
    a = Merkki(5, 5, "A")
    b = Merkki(9, 2, "B")

    while True:
        for rivi in kartta:
            for alkio in rivi:
                print(f"{alkio},", end=" ")
            print("")

        liiku = input(">")

        if liiku == "d":
            a.liiku_oikea()
        elif liiku == "a":
            a.liiku_vasen()
        elif liiku == "w":
            a.liiku_ylos()
        elif liiku == "s":
            a.liiku_alas()
        elif liiku == "p":
            break

        if a.x == b.x and a.y == b.y:
            break

if __name__ == "__main__":
    main()