class Auto:

    # Konstruktori, joka alustaa auton rekisterinumeron, huippunopeuden, hetkellisen nopeuden ja kuljetun matkan
    def __init__(self, rekisterinumero, huippunopeus, hetkellinen_nopeus, kuljettu_matka):
        self.rekisterinumero = rekisterinumero
        self.huippunopeus = huippunopeus
        self.hetkellinen_nopeus = hetkellinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def __str__(self):
        return f"Auto {self.rekisterinumero} on kulkenut {self.kuljettu_matka} km/h ja sen hetkellinen nopeus on {self.hetkellinen_nopeus} km/h."

    # Metodi, joka laskee auton nopeuden muutoksen joka voi olla joko positiivinen tai negatiivinen eikä koskaan yli huippunopeuden
    def kiihdyta(self, muutos):
        if self.hetkellinen_nopeus + muutos > self.huippunopeus:
            self.hetkellinen_nopeus = self.huippunopeus
        elif self.hetkellinen_nopeus + muutos < 0:
            self.hetkellinen_nopeus = 0
        else:
            self.hetkellinen_nopeus += muutos

    # Kulje metodi jossa parametrina tuntimaara ja lasketaan kuljettu matka nopeuden perusteella
    def kulje(self, tuntimaara):
        self.kuljettu_matka += self.hetkellinen_nopeus * tuntimaara

# Testataan Auto-luokkaa
auto = Auto("ABC-123", 200, 60, 2000)
print(auto)

auto.kulje(1.5)
print(auto)





