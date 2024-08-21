kevat_kuukaudet = ("Maalis", "Huhti", "Touko")
kesa_kuukaudet = ("Kesä", "Heinä", "Elo")
syksy_kuukaudet = ("Syys", "Loka", "Marras")
talvi_kuukaudet = ("Joulu", "Tammi", "Helmi")

kuukauden_numero = int(input("Anna kuukauden numero: "))

if kuukauden_numero in range(3, 6):
    print(kevat_kuukaudet[kuukauden_numero - 3])
elif kuukauden_numero in range(6, 9):
    print(kesa_kuukaudet[kuukauden_numero - 6])
elif kuukauden_numero in range(9, 12):
    print(syksy_kuukaudet[kuukauden_numero - 9])
else:
    print(talvi_kuukaudet[kuukauden_numero - 12])



