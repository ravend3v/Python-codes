lentoasemat = {"EFHK":"Helsinki-Vantaa"}

while True:
    print("1) Lisää lentoasema")
    print("2) Hae lentoasema")
    print("3) Lopeta")
    valinta = input("Valitse toiminto: ")

    if valinta == "1":
        lentoasema = input("Anna lisättävän lentoaseman ICAO-koodi: ")
        if lentoasema in lentoasemat:
            print("Lentoasema on jo lisätty")
        else:
            lentoasemat[lentoasema] = lentoasema
            print("Lentoasema lisätty")
    elif valinta == "2":
        lentoasema = input("Anna lentoaseman ICAO-koodi: ")
        if lentoasema in lentoasemat:
            print(lentoasemat[lentoasema])
        else:
            print("Lentoasemaa ei löytynyt")
    elif valinta == "3":
        break
    else:
        print("Virheellinen valinta, yritä uudelleeen")
        continue