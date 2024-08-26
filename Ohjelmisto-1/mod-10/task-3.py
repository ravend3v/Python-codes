# Hissi sovellus tehtävä 3 jatko osa tehtävästä 2

class Hissi:
    def __init__(self, alin_kerros=1, ylin_kerros=5):
        self.ylin_kerros = ylin_kerros
        self.alin_kerros = alin_kerros

    def siirry_kerrokseen(self, kerros):
        if kerros > 5:
            self.kerros = 5
        elif kerros < 1:
            self.kerros = 1
        else:
            self.kerros = kerros

    def kerro_ylos(self):
        if self.kerros < 5:
            self.kerros += 1

    def kerros_alas(self):
        if self.kerros > 1:
            self.kerros -= 1

    def __str__(self):
        return f"Hissi on kerroksessa {self.kerros}"

# Talo luokka
class Talo:
    # Konstruktori alustaa talon hissit
    def __init__(self, alin_kerros=1, ylin_kerros=5, hissit=1):
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissit)]

    # Metodi joka ajaa hissiä
    def aja_hissia(self, hissi, kerros):
        self.hissit[hissi].siirry_kerrokseen(kerros)

    def palohalytys(self):
        pohja_kerros = 1
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(pohja_kerros)

    # Metodi joka palauttaa hissien määrän
    def __str__(self):
        return f"Talossa on {len(self.hissit)} hissiä"

talo = Talo(1, 5, 2)

def main():
    print(talo)
    talo.aja_hissia(0, 3)
    print(talo.hissit[0])
    talo.aja_hissia(1, 5)
    print(talo.hissit[1])

    print("Palohälytys!")
    talo.palohalytys()
    print(talo.hissit[0])

if __name__ == "__main__":
    main()
