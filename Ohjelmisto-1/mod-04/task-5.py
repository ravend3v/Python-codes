käyttäjätunnus = []
salasana = []

def rekisteröidy():
    print("Rekisteröidy")
    käyttäjätunnus.append(input("Syötä käyttäjätunnus: "))
    salasana.append(input("Syötä salasana: "))
    print("Rekisteröinti onnistui!")

def kirjaudu():
    while True:
        anna_tunnus = input("Syötä käyttäjätunnus: ")
        anna_salasana = input("Syötä salasana: ")
        if anna_tunnus in käyttäjätunnus and anna_salasana in salasana:
            print("Tervetuloa")
            break
        else:
            print("Pääsy evätty")

def main():
    rekisteröidy()
    kirjaudu()

if __name__ == "__main__":
    main()
    