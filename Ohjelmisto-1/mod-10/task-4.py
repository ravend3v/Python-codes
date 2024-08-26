# Jatkoa moduuli 09 autokilpailu tehtävälle

import random

autot = []

class Auto:
    def __init__(self):
        self.__nopeus = 0
        self.__rekisterinumero = ""
        self.__kuljettuMatka = 0

    def setNopeus(self, nopeus):
        self.__nopeus = nopeus

    def setRekisterinumero(self, rekisterinumero):
        self.__rekisterinumero = rekisterinumero

    def setKuljettuMatka(self, matka):
        self.__kuljettuMatka = matka

    def kiihdyta(self, nopeus):
        self.__nopeus += nopeus

    def kulje(self, matka):
        self.__kuljettuMatka += matka

    def getNopeus(self):
        return self.__nopeus

    def getRekisterinumero(self):
        return self.__rekisterinumero

    def getKuljettuMatka(self):
        return self.__kuljettuMatka

# Luodaan 10 autoa
for i in range(10):
    auto = Auto()
    auto.setNopeus(random.randint(100, 200))

    # Asetetaan rekisterinumero järjestyksessä ABC-1 -> ABC-10
    rekisterinumero = "ABC-" + str(i + 1)
    auto.setRekisterinumero(rekisterinumero)
    autot.append(auto)

class Kilpailu:
    def __init__(self, kilpailun_nimi, pituus_km, osallistuvat_autot):
        self.__kilpailun_nimi = kilpailun_nimi
        self.__pituus_km = pituus_km
        self.__osallistuvat_autot = osallistuvat_autot

    def tunti_kuluu(self):
        for auto in self.__osallistuvat_autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(auto.getNopeus())
        return self.__osallistuvat_autot[0].getRekisterinumero()

    def tulosta_tilanne(self):
        print(f"{'Resskiterinumero ':<15}{'Nopeus (km/h)':<15}{'Kuljettu matka (km)':<20}")
        for auto in self.__osallistuvat_autot:
            print(f"{auto.getRekisterinumero():15}{auto.getNopeus():<15}{auto.getKuljettuMatka():<20}")
        print()

    def kilpailu_ohi(self):
        for auto in self.__osallistuvat_autot:
            if auto.getKuljettuMatka() >= self.__pituus_km:
                return True
        return False

def main():
    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)
    kilpailu.tulosta_tilanne()

    tunnit = 0
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        tunnit += 1
        if tunnit % 10 == 0:
            kilpailu.tulosta_tilanne()

    print("Kilpailun voittaja on", kilpailu.tunti_kuluu())
    print()
    # Tulostetaan lopullinen tilanne
    kilpailu.tulosta_tilanne()

main()



