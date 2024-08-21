kokonaisluku = int(input("Anna kokonaisluku: "))

# Tarkistetaan onko luku jaollinen itsellään ja luvulla 1 for loopilla
for i in range(2, kokonaisluku):
    if kokonaisluku % i == 0:
        print("Luku ei ole alkuluku.")
        break
else:
    print("Luku on alkuluku.")

