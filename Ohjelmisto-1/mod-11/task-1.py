class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara


    def tulosta_tiedot(self):
        print(f"{self.nimi}, kirjoittanut {self.kirjoittaja}, {self.sivumaara} sivua")

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"{self.nimi}, päätoimittaja {self.paatoimittaja}")

def main():
    kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
    lehti = Lehti("Aku Ankka", "Aki Hyyppä")

    kirja.tulosta_tiedot()
    lehti.tulosta_tiedot()

if __name__ == "__main__":
    main()

