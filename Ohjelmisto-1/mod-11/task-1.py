class Julkaisu:

    class Kirja:
        def __init__(self, nimi, kirjoittaja, sivumaara):
            self.nimi = nimi
            self.kirjoittaja = kirjoittaja
            self.sivumaara = sivumaara

        def tulosta_tiedot(self):
            print(f"Kirja: {self.nimi}\nKirjoittaja: {self.kirjoittaja}\nSivumäärä: {self.sivumaara}")

    class Lehti:
        def __init__(self, nimi, paatoimittaja):
            self.nimi = nimi
            self.paatoimittaja = paatoimittaja

        def tulosta_tiedot(self):
            print(f"Lehti: {self.nimi}\nPäätoimittaja: {self.paatoimittaja}")


def main():
    kirja = Julkaisu.Kirja("Hytti n:o 6", "Rosa Liksom", 200)
    lehti = Julkaisu.Lehti("Aku Ankka", "Aki Hyyppä")

    lehti.tulosta_tiedot()
    print()
    kirja.tulosta_tiedot()

if __name__ == "__main__":
    main()