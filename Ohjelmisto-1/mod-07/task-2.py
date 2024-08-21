nimet = set()

while True:
    nimi = str(input("Anna nimi: "))
    if nimi == "":
        break

    if nimi not in nimet:
        print("Uusi nimi")
        nimet.add(nimi)

    else:
        print("Aiemmin syötetty nimi")

print("Nimet: ", nimet)



