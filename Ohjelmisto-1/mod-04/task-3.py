numerot = []

while True:


    numero = input("Anna numero: ")

    #jos käyttäjä ei anna mitään, lopetetaan ohjelma
    if numero == "":
        break
    else:
        numerot.append(int(numero))


#printataan isoin ja pienin numero
print("Pienin numero: ", min(numerot))
print("Suurin numero: ", max(numerot))

