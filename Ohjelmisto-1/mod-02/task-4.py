#Pyydetään loopilla 3 lukua käyttäjältä ja lasketaan summa, tulo ja keskiarvo.
for i in range(3):
    luku = int(input("Anna luku: "))
    if i == 0:
        summa = luku
        tulo = luku
    else:
        summa += luku
        tulo *= luku
keskiarvo = summa / 3
print(f"Summa: {summa}")
print(f"Tulo: {tulo}")
print(f"Keskiarvo: {keskiarvo}")
