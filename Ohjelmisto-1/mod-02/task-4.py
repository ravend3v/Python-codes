#Pyydetään loopilla 3 lukua käyttäjältä ja lasketaan summa, tulo ja keskiarvo.
for i in range(3):
    luku = int(input("Anna luku: "))

    # Asetetaan summa ja tulo luvun arvoksi.
    if i == 0:
        summa = luku
        tulo = luku

    # Lasketaan summa ja tulo.
    else:
        summa += luku
        tulo *= luku

# Lasketaan keskiarvo.
keskiarvo = summa / 3

# Tulostetaan summa, tulo ja keskiarvo.
print(f"Summa: {summa}")
print(f"Tulo: {tulo}")
print(f"Keskiarvo: {keskiarvo}")
