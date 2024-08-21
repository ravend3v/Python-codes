import random as rnd

oikea_numero = rnd.randint(1, 10)

while True:
    arvaus = int(input("Arvaa luku väliltä 1-10: "))

    if arvaus > oikea_numero:
        print("Liian suuri arvaus!")

    elif arvaus < oikea_numero:
        print("Liian pieni arvaus!")

    else:
        print("Oikein!")
        break
        