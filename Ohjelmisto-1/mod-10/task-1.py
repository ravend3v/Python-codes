# Hissi sovellus tehtävä 1 ensimmäinen osa

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

hissi_kerrokset = [1, 2, 3, 4, 5]

def main():
    hissi = Hissi()
    print(f"Hissin kerrokset: {hissi_kerrokset}")
    hissi.siirry_kerrokseen(5)
    print(hissi)
    hissi.siirry_kerrokseen(1)
    print(hissi)

if __name__ == "__main__":
    main()
