# Jatkoa mod-08 auto-luokalle
class Auto:
    def __init__(self, rekisterinumero, nopeus, kuljettu_matka, hetkellinen_nopeus):
        self.rekisterinumero = rekisterinumero
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka
        self.hetkellinen_nopeus = hetkellinen_nopeus

    def kulje(self, tuntimaara):
        self.kuljettu_matka += self.hetkellinen_nopeus * tuntimaara

class Sahko(Auto):
    def __init__(self, rekisterinumero, nopeus, akun_kapasiteetti, kuljettu_matka, hetkellinen_nopeus):
        super().__init__(rekisterinumero, nopeus, kuljettu_matka, hetkellinen_nopeus)
        self.akun_kapasiteetti = akun_kapasiteetti

    def __str__(self):
        return f"Rekisterinumero: {self.rekisterinumero}, Nopeus: {self.nopeus}, Akun kapasiteetti: {self.akun_kapasiteetti}"

class Polttomoottori(Auto):
    def __init__(self, rekisterinumero, nopeus, polttoaineen_tilavuus, kuljettu_matka, hetkellinen_nopeus):
        super().__init__(rekisterinumero, nopeus, kuljettu_matka, hetkellinen_nopeus)
        self.polttoaineen_tilavuus = polttoaineen_tilavuus

    def __str__(self):
        return f"Rekisterinumero: {self.rekisterinumero}, Nopeus: {self.nopeus}, Polttoaineen tilavuus: {self.polttoaineen_tilavuus}"

def main():
    sahko_auto = Sahko("ABC-123", 100, 100, 0, 50)
    polttomoottori_auto = Polttomoottori("DEF-456", 200, 50, 0, 100)

    sahko_auto.kulje(3)
    polttomoottori_auto.kulje(3)
    print()
    print(f"Sähköauto: {sahko_auto.kuljettu_matka} km")
    print(f"Polttomoottoriauto: {polttomoottori_auto.kuljettu_matka} km")

if __name__ == "__main__":
    main()