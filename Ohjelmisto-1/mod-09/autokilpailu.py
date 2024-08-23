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

# Arvotaan nopeuden muutos jokaiselle autolle väliltä -10 ja 15 käytetään kiihdytä-metodia
for auto in autot:
    nopeudenMuutos = random.randint(-10, 15)
    auto.kiihdyta(nopeudenMuutos)

# Käsketään autoja liikkumaan 1 tunnin ajan, kilpailu jatkuu kunnes joku auto on kulkenut 10000 kilometriä
kilometrit = 0
while True:
    for auto in autot:
        auto.kulje(auto.getNopeus())
        if auto.getKuljettuMatka() >= 10000:
            print("Voittaja on auto", auto.getRekisterinumero())
            print()
            break
    else:
        continue
    break

# Tulostetaan kaikkien autojen tiedot selkeänä taukona
for auto in autot:
    print("Rekisterinumero:", auto.getRekisterinumero())
    print("Nopeus:", auto.getNopeus())
    print("Kuljettu matka:", auto.getKuljettuMatka())
    print()




