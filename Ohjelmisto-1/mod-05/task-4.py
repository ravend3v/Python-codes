kaupunki_lista = []

for i in range(5):
    kaupungit = str(input("Anna kaupunki: "))
    kaupunki_lista.append(kaupungit)

#printataan kaupungit allekkain syöttöjärjestyksessä
for i in kaupunki_lista:
    print(i)