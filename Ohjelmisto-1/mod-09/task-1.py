class Auto:
    def __init__(self, rekisterinumero, huippunopeus, hetkellinen_nopeus, kuljettu_matka):
        self.rekisterinumero = rekisterinumero
        self.huippunopeus = huippunopeus
        self.hetkellinen_nopeus = hetkellinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def __str__(self):
        return f"Auto {self.rekisterinumero} on kulkenut {self.kuljettu_matka} km/h ja sen hetkellinen nopeus on {self.hetkellinen_nopeus} km/h."


auto = Auto("ABC-123", 142, 100, 1000)

print(auto)
